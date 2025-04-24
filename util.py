import os


def get_secret(env_var: str, default: str | None = None) -> str | None:
    path = os.getenv(env_var)
    if path is None:
        print(f"Env variable {env_var} is not set. Using insecure default")
        return default
    else:
        with open(path, "r") as f:
            return f.read().strip()
