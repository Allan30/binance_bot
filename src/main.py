import asyncio
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Choose which module to use.")

    parser.add_argument('-m', '--module', required=True, help="Module name to launch")

    args = parser.parse_args()

    if args.module == 'agent_receiver_kline_stream':
        from src.scripts.agent_stream_receiver import AgentStreamReceiver
        agent = AgentStreamReceiver(
            "test",
            "test",
            "wss://fstream.binance.com/ws/btcusdt@kline_1m"
        )
        asyncio.run(agent.run())
    else:
        print(f"Module {args.module} unknow")
        sys.exit(1)

if __name__ == "__main__":
    main()


