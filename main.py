from app.daily_runner import run_daily_pipeline


def main(hours: int = 24, top_n: int = 10):
    return run_daily_pipeline(hours=hours, top_n=top_n)


# ...existing code...
if __name__ == "__main__":
    import sys
    
    hours = 48
    top_n = 10
    

    is_interactive = any(arg.startswith('-f') or arg.endswith('.json') for arg in sys.argv)

    if not is_interactive:
        if len(sys.argv) > 1:
            try:
                hours = int(sys.argv[1])
            except ValueError:
                pass
        if len(sys.argv) > 2:
            try:
                top_n = int(sys.argv[2])
            except ValueError:
                pass
    
    print(f"Running pipeline with hours={hours}, top_n={top_n}")
    result = main(hours=hours, top_n=top_n)
    
    
    if not is_interactive:
        exit(0 if result["success"] else 1)