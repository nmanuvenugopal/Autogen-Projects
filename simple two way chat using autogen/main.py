import autogen
import pandas as pd

def main():
    try:
        # Declaring the configuration list
        config_list = autogen.config_list_from_json(
            env_or_file="Config_List.json"
        )

        # Now we need to create an Autogen assistant
        assistant = autogen.AssistantAgent(
            name="Assistant",
            llm_config={
                "config_list": config_list
            }
        )

        # Define the user proxy for the Autogen
        user_proxy = autogen.UserProxyAgent(
            name="user",
            human_input_mode="NEVER",
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False
            }
        )

        # Everything set, now we need to ask Autogen Assistant to do some tasks
        user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
