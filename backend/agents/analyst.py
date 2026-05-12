from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


class AnalystAgent:

    def analyze(self, content: str):

        prompt = f"""
        请分析以下运营计划：

        {content}

        输出：
        1. 风险
        2. 优化建议
        3. ROI判断
        """

        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an analyst agent"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return res.choices[0].message.content
