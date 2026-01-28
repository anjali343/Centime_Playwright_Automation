class Config:
    BASE_URL = "https://www.saucedemo.com/"
    HEADED = False
    DEFAULT_BROWSER = "chromium"
    DEFAULT_TRACING = False
    # Tracing options
    TRACE_OPTIONS = {
        "screenshots": True,
        "snapshots": True,
        "sources": True,
    }