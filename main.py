import asyncio
from src.graph import graph
from langchain_core.messages import HumanMessage


async def main():
    # コンパイル
    app = graph.compile()

    # 初期状態の準備
    initial_state = {
        "messages": [HumanMessage(content="今日の東京の天気を教えて")],
        "search_queries": [],
        "search_results": [],
        "attempt": 0
    }
    # エージェントの実行
    result = await app.ainvoke(initial_state)
    # 結果の取得
    print(f"回答: {result['response']}")

    return result


if __name__ == "__main__":
    asyncio.run(main())