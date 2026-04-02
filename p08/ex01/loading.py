import importlib
import sys


def check_dependencies() -> dict[str, tuple[bool, str | None]]:
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    status: dict[str, tuple[bool, str | None]] = {}

    for pkg in packages:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            status[pkg] = (True, version)
        except ImportError:
            status[pkg] = (False, None)
    return status


def compare_installed_versions() -> dict[str, str | None]:
    """Collect the installed package versions used in the analysis."""
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    status = check_dependencies()

    versions: dict[str, str | None] = {}
    for pkg in packages:
        installed, version = status[pkg]
        if installed:
            versions[pkg] = version
        else:
            versions[pkg] = None

    return versions


def load_matrix_data() -> None:
    """Run the sample Matrix analysis and save a chart."""
    pandas_module = importlib.import_module("pandas")
    numpy_module = importlib.import_module("numpy")
    matplotlib_module = importlib.import_module("matplotlib")

    matplotlib_module.use("Agg")
    pyplot_module = importlib.import_module("matplotlib.pyplot")

    print("Analyzing Matrix data...")
    data = numpy_module.random.randn(1000)
    df = pandas_module.DataFrame(data, columns=["Signal Strength"])

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt_data = df.rolling(window=50).mean()

    pyplot_module.figure(figsize=(10, 6))
    pyplot_module.plot(plt_data, color="green", label="Matrix Signal")
    pyplot_module.title("Matrix Data Analysis")
    pyplot_module.xlabel("Data Points")
    pyplot_module.ylabel("Signal Strength")
    pyplot_module.legend()
    pyplot_module.grid(True, linestyle="--", alpha=0.7)

    output_file = "matrix_analysis.png"
    pyplot_module.savefig(output_file)
    pyplot_module.close()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """Check package availability and run the loading demo."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready"
    }

    status = check_dependencies()
    versions = compare_installed_versions()
    all_installed = True

    for pkg, (installed, version) in status.items():
        if installed:
            desc = descriptions.get(pkg, "Ready")
            display_version = versions.get(pkg) or version or "unknown"
            print(f"[OK] {pkg} ({display_version}) - {desc}")
        else:
            print(f"[MISSING] {pkg} - Not found!")
            all_installed = False

    if not all_installed:
        print("\nERROR: Some programs are missing."
              " The simulation cannot start.")
        print("To fix this, choose a pill:")
        print("1. PIP:    pip install -r requirements.txt")
        print("2. POETRY: poetry install")
        sys.exit(1)

    try:
        load_matrix_data()
    except Exception as e:
        print(f"A glitch occurred during loading: {e}")


if __name__ == "__main__":
    main()
