def generate(version, changelog_items):
    return '\n'.join([
        __generate_header(version),
        __generate_items_list(changelog_items)
    ])

def __generate_header(version):
    return f'## {version}\n'

def __generate_items_list(changelog_items):
    return '\n'.join(list(map(lambda item: f'* {item}', changelog_items)))
