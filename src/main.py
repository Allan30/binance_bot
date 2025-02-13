import asyncio
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Choisissez un module à utiliser.")

    parser.add_argument('-m', '--module', required=True, help="Module name to launch")

    args = parser.parse_args()

    if args.module == 'scheduler':
        from src.scripts.trade_scheduler import TradeScheduler
        scheduler = TradeScheduler()
        asyncio.run(scheduler.run())
    else:
        print(f"Module {args.module} unknow")
        sys.exit(1)

if __name__ == "__main__":
    main()


