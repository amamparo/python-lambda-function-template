from typing import Optional


def main() -> None:
    print('hello world')


# pylint: disable=unused-argument
def lambda_handler(event: Optional[dict] = None, context: Optional[dict] = None) -> None:
    main()


if __name__ == '__main__':
    main()
