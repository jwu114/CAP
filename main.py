from tqdm import tqdm
from config import para, path
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import random, json, base64, re
import argparse
from openai import OpenAI

def sample(file, dataset, size):
    dataset_sampled = random.sample(dataset, size)
    for item in tqdm(dataset_sampled, desc="Writing File"):
        file.write(json.dumps(item) + '\n')
    return dataset_sampled

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def evaluate(dataset, prompt, args):
    gt_labels, p_labels = [], []
    client = OpenAI(api_key = args.key)

    for item in tqdm(dataset, desc="Evaluating"):
        if item["image"].startswith("https:") or item["image"].startswith("http:"):
            url = {"url": item["image"],}
        else:
            image = encode_image(path.dataset / args.dataset / item["image"])
            url = {"url": f"data:image/jpeg;base64,{image}",}
        count = 0
        while count < 10:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-2024-05-13",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt + item["text"]},
                                {
                                    "type": "image_url",
                                    "image_url": url,
                                },
                            ],
                        }
                    ],
                    max_tokens=1024,
                    temperature = 1e-15,
                    top_p = 1e-15,
                    seed = 124,
                )
                break
            except Exception:
                print(Exception)
                print("ERROR")
                count += 1
                continue
            
        res = response.choices[0].message.content
        res_archive = res
        
        res = re.sub(r'\W+', ' ', res.splitlines()[-1]).lower()
        ans = res.split()
        has_Yes = "yes" in ans
        has_No = "no" in ans
        gt = item['label']

        if has_Yes and has_No:
            if "image" in ans: # xxx not in the image
                p_labels.append(0)
            else:
                p_labels.append(-1)
                print("ERROR")
                print(res_archive)
        elif has_Yes:
            p_labels.append(1)
        elif has_No:
            p_labels.append(0)
        else:
            if "image" in ans: # xxx not in the image
                p_labels.append(0)
            else:
                print("ERROR")
                p_labels.append(-1)
                print(res_archive)
                
        if gt == 'yes':
            gt_labels.append(1)
        else:
            gt_labels.append(0)
                
    # print results
    print(p_labels)
    print()
    
    # evaluate
    # calculate accuracy
    accuracy = accuracy_score(gt_labels, p_labels)
    print(f"Accuracy: {accuracy * 100:.2f}%", end=" ")
    # calculate precision
    precision = precision_score(gt_labels, p_labels)
    print(f"Precision: {precision * 100:.2f}%", end=" ")
    # calculate recall
    recall = recall_score(gt_labels, p_labels)
    print(f"Recall: {recall * 100:.2f}%", end=" ")
    # calculate F1 score
    f1 = f1_score(gt_labels, p_labels)
    print(f"F1 Score: {f1 * 100:.2f}%")
    
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments")
    parser.add_argument('--dataset', type=str, default='mmrel', help='aro/gqa/mmrel')
    parser.add_argument('--test', action='store_true', help='test/valid')
    parser.add_argument('--prompt', type=int, default=0, help="check config/para")
    parser.add_argument('--key', type=str, default='', help='openai_key')
    
    args = parser.parse_args()
    if args.key == "":
        print("Please include your OpenAI key in arguments")
        quit()
    
    dataset_path = path.dataset / args.dataset / "annotation" / (("test" if args.test else "valid") + ".jsonl")
    
    # build dataset
    with open(dataset_path, 'r') as sample_file:
        dataset = [json.loads(item) for item in tqdm(sample_file, desc="Loading File")]
    random.shuffle(dataset)
    
    # create prompt
    prompt = para.prompts_vqa[args.prompt]

    # evaluate with gpt4
    evaluate(dataset, prompt, args)

    
