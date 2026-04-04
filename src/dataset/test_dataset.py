from src.dataset.generator import generate_elements
from src.core.aabb_clash import detect_clashes


def run_dataset_test():

    elements = generate_elements(50)

    print(f"\nGenerated {len(elements)} elements\n")

    clashes = detect_clashes(elements)

    print(f"Detected {len(clashes)} clashes\n")

    for clash in clashes[:10]:
        print(clash)


if __name__ == "__main__":
    run_dataset_test()