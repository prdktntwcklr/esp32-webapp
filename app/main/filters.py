from . import main


@main.app_template_filter('splitstr')
def splitstr_filter(text: str) -> list[str]:
    return text.split('\n')
