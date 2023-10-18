from app.config import settings


def setup_debugger():
    try:
        import pydevd_pycharm
        pydevd_pycharm.settrace(host=settings.HOST_DEBUG, port=12345, stdoutToServer=True, stderrToServer=True,
                                suspend=False)
        print("Connected to the debugger at port 12345")
    except Exception as e:
        print(f"Failed to connect to the debugger: {e}")
