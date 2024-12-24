from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent = Agent(
    model = Groq(id="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use table to display data."]
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")

