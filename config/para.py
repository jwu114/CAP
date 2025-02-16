openai_key = "" # replace with your own key
sample_size = 600

"""
prompts_vqa
0: baseline (vanilla)
1: baseline (CoT+structure)
2: AB
3: BA
4: AB+BA
5: BA+AB (bidirectional)
6: AC+BC (transitivity)
7: AC+BC+AB
8: AC+BC+BA
9: AC+BC+AB+BA
10: AC+BC+BA+AB (combined)
"""

"""
prompts_attribute_transitivity & prompts_attribute_combined
0: the largest
1: the smallest
2: the most top
3: the central
4: the most obvious
"""

"""
prompts_nocot & prompts_nostructure
0: transitivity
1: bidirectional
2: combined
"""

prompts_vqa = [
"Use 'yes' or 'no' to answer the question: ",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Think step by step to use 'yes' or 'no' to answer the question.
## Please output in the following format ##
Question:
Object A:
Object B:
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the relative position between Object A and B.
3. Reference to the relationship between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the relative position between Object B and A.
3. Reference to the relationship between Object B and A, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the relative position between Object A and B and between Object B and A.
3. Reference to the relationship between Object A and B and between Object B and A, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the relative position between Object B and A and between Object A and B.
3. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object A and B.
4. Reference to the relationship between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A.
4. Reference to the relationship between Object B and A, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object A and B and between Object B and A.
4. Reference to the relationship between Object A and B and between Object B and A, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
]

prompts_attribute_transitivity = ["""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the largest object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the smallest object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the most top object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the central object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the most obvious object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Thinking process: 
Answer: 

## Question ##
"""]

prompts_attribute_combined = [
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the largest object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the smallest object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the most top object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the central object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select the most obvious object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Thinking process: 
Answer: 

## Question ##
"""
]

prompts_nocot = [
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the relative position between Object B and A and between Object A and B.
3. Reference to the relationship between Object B and A and between Object A and B, and then use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Answer: 

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then use 'yes' or 'no' to answer the question.

## Please output in the following format ##
Question:
Object A:
Object B:
Object C:
Horizontal relation between Object A and C: A is <relation> C
Vertical relation between Object A and C: A is <relation> C
Depth relation between Object A and C: A is <relation> C
Horizontal relation between Object B and C: B is <relation> C
Vertical relation between Object B and C: B is <relation> C
Depth relation between Object B and C: B is <relation> C
Horizontal relation between Object B and A: B is <relation> A
Vertical relation between Object B and A: B is <relation> A
Depth relation between Object B and A: B is <relation> A
Horizontal relation between Object A and B: A is <relation> B
Vertical relation between Object A and B: A is <relation> B
Depth relation between Object A and B: A is <relation> B
Answer: 

## Question ##
""",
]

prompts_nostructure = [
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the horizontal, vertical, and depth relative position between Object A and C and between Object B and C.
3. Reference to the relationship between Object A and C and between Object B and C, and then think step by step to use 'yes' or 'no' to answer the question.

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B".
2. Describe the horizontal, vertical, and depth relative position between Object B and A and between Object A and B.
3. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Question ##
""",
"""## Instructions ##
1. Repeat the question and then extract the objects mentioned in the question. Label the first object that appears as "Object A" and the second as "Object B". Select an object different from Object A or Object B in the image as "Object C"
2. Describe the horizontal, vertical, and depth relative position between Object A and C and between Object B and C.
3. Reference to the result of step 2 and image, describe the relative position between Object B and A and between Object A and B.
4. Reference to the relationship between Object B and A and between Object A and B, and then think step by step to use 'yes' or 'no' to answer the question.

## Question ##
""",
]