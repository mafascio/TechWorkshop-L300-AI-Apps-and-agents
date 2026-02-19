

### Custom attack objectives
## The Azure AI Red Teaming Agent includes a set of predefined attack objectives that cover a range of common risks and vulnerabilities. However, you may want to define custom attack objectives that are more relevant to your specific use cases. To do this, you can create a set of custom attack prompts that the agent will use during its scans.

# Azure imports
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from pyrit.prompt_target import OpenAIChatTarget
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

# Azure AI Project Information
azure_ai_project = os.getenv("FOUNDRY_ENDPOINT")

# Instantiate your AI Red Teaming Agent
# red_team_agent = RedTeam(
#     azure_ai_project=azure_ai_project,
#     credential=DefaultAzureCredential(),
#     risk_categories=[
#         RiskCategory.Violence,
#         RiskCategory.HateUnfairness,
#         RiskCategory.Sexual,
#         RiskCategory.SelfHarm
#     ],
#     num_objectives=5,
# )


# # 
# Inside of the src/data/ directory, open the file custom_attack_prompts.json. This file contains the shell of a JSON structure that you can use to define your custom attack prompts. The file contains one example in the violence category. Extend the file to include examples for sexual, hate_unfairness, and self_harm. You may include as many examples as you wish for each category.
# #

red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project,
    credential=DefaultAzureCredential(),
    custom_attack_seed_prompts="data/custom_attack_prompts.json",
)

# azure_openai_config = { 
#     "azure_endpoint": f"{os.environ.get('gpt_endpoint')}/openai/deployments/{os.environ.get('gpt_deployment')}/chat/completions",
#     "api_key": os.environ.get("FOUNDRY_KEY"),
#     "azure_deployment": os.environ.get("gpt_deployment")
# }

chat_target = OpenAIChatTarget(
    model_name=os.environ.get("gpt_deployment"),
    endpoint=f"{os.environ.get("gpt_endpoint")}/openai/deployments/{os.environ.get('gpt_deployment')}/chat/completions" ,
    api_key=os.environ.get("gpt_api_key"),
    api_version=os.environ.get("gpt_api_version"),
)

# def test_chat_target(query: str) -> str:
#     return "I am a simple AI assistant that follows ethical guidelines. I'm sorry, Dave. I'm afraid I can't do that."

async def main():
    red_team_result = await red_team_agent.scan(target=chat_target)
    # red_team_result = await red_team_agent.scan(target=azure_openai_config)
    # red_team_result = await red_team_agent.scan(target=test_chat_target)

asyncio.run(main())
# cd src
# python app/agents/redTeamingAgent_initializer.py