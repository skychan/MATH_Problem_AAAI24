# How to use ToRA to inference

1. Clone ToRA's code here

   ```
   git clone https://github.com/microsoft/ToRA.git
   ```

2. Follow the official instuctions to configure the environment and install all the requirements.

3. Download the question data as `TAL-SAQ6K-EN.jsonl`

4. Run the preprocessing code:

   ```
   python pre_process.py
   ``` 

   and you will generate `TAL-SAQ6K-EN_mod.jsonl`

5. Create new test data for ToRA

   ```
   mkdir -p ToRA/src/data/tal
   mv TAL-SAQ6K-EN_mod.jsonl ToRA/src/data/tal/test.jsonl
   ```

6. Copy the inference scripts

   ```
   cp inference.py ToRA/src/infer/inference_tal.py
   cp infer_tal.sh ToRA/src/scripts/
   ```

7. Run the inference script

   ```
   cd ToRA/src
   bash scripts/infer_tal.sh
   ```

8. Wait for a while, the result(s) will be in `ToRA/src/output/llm-agents/tora-code-34b-v1.0/tal/`

9. Copy out the results

   ```
   # current path is ToRA/src
   cd ../../
   cp -r ToRA/src/output/llm-agents/tora-code-34b-v1.0/tal/ results
   ```

10. Convert the result to the submission, let's say your result is `results/test_tora_5927_seed13_t0.0_s0_e5927_12-29_14-11.jsonl`

    ```
    python post_process.py --answer results/test_tora_5927_seed13_t0.0_s0_e5927_12-29_14-11.jsonl
    ```

    Then you will get `TAL_SAQ6K_EN_prediction.jsonl`
