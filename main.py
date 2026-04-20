import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from configs.prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"

def _get_model_response(model, messages):
    try:
        response = client.models.generate_content(
            model=model,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt, 
                temperature=0
            ),
        )
        return response
    except Exception as e:
        print(f"[Error] failed getting model response: {e.code}")
        print(f"[Error] message: {e.message}")
        print(f"[Error] details: {e.details}")

def main():
    print("Hello from ai-agent-demo-02!")

    # custom_prompt = """Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."""
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    args = parser.parse_args()
    custom_prompt = args.user_prompt
    verbose_flag = args.verbose
    messages = [types.Content(role="user", parts=[types.Part(text=custom_prompt)])]

    for _ in range(20):
        response = _get_model_response(model, messages)
        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return
        
        if verbose_flag:
            prompt_token_cnt = response.usage_metadata.prompt_token_count
            candidates_token_cnt = response.usage_metadata.candidates_token_count
            
            print(f"User prompt: {messages}")
            print(f"Prompt tokens: {prompt_token_cnt}")
            print(f"Response tokens: {candidates_token_cnt}")
        
        """
        We need to ensure that, in each iteration of the loop, 
        the model is aware of all the messages and tool requests that it has generated so far. 
        Each response from the Gemini API has a .candidates property 
        - a list of the model's response(s) to the last prompt (usually just one). 
        Add all "candidates" to the conversation history so the model can see them in future iterations.
        """
        if response.candidates:
            for candidate in response.candidates:
                # print(f"[DEBUG] candidate content: {candidate.content}")
                messages.append(candidate.content)
                for part in candidate.content.parts:
                    if part.text:
                        print(f"Response: {response.text}")
        
        # if response.text:
        #     print(f"Response: {response.text}")
        
        function_call_result_list = []
        if response.function_calls:
            for function_call in response.function_calls:
                # print(f"Calling function: {function_call.name}({function_call.args})")
                function_call_result = call_function(function_call, verbose_flag)
                if not function_call_result.parts:
                    raise Exception
                if not function_call_result.parts[0].function_response:
                    raise Exception
                if not function_call_result.parts[0].function_response.response:
                    raise Exception
                function_call_result_list.append(function_call_result.parts[0])
                if verbose_flag:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                
                """
                The model will also need to see the results of any function calls that it makes. 
                You should already be collecting a list of function results.
                """
                messages.append(function_call_result)
        else:
            return


if __name__ == "__main__":
    main()
