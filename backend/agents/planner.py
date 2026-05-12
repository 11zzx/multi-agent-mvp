from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


class PlannerAgent:

    def run(self, task: str):

        prompt = f"""
        你是任务拆解 Agent。

        用户需求：
        {task}

        请拆解为：
        1. 数据分析
        2. 内容生成
        3. 推广动作

        使用简洁 JSON 返回。
        """

        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a planning agent"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return res.choices[0].message.content
