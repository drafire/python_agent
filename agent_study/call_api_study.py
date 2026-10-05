import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage, ChatCompletionUserMessageParam, \
    ChatCompletionAssistantMessageParam, ChatCompletionSystemMessageParam

client = OpenAI(
    api_key=os.getenv("ZHI_PU_KEY"),
    base_url=os.getenv("ZHI_PU_URL")
)
try:
    response = client.chat.completions.create(
        model="glm-4",  # 模型名称
        messages=[
            ChatCompletionUserMessageParam(role="user", content="你好，请帮我写一首诗"),
            ChatCompletionAssistantMessageParam(role="assistant", content="好的，我是你的AI助手？"),
            ChatCompletionSystemMessageParam(role="system",content="你是一个诗人")
        ],
        temperature=0.8,  # 控制生成文本的随机性，值越高越随机
        stream=True  # 是否流式输出
    )
    # print(response.choices[0].message.content)  # 这个是直接输出
    for chunk in response:
        content= chunk.choices[0].delta.content
        if content is not None:
            print(content, end='',flush=True)  #实时打印
except Exception as e:
    print(e)
