def collect_text(children, text_key='text'):
    parts = []
    for child in children or []:
        if text_key in child:
            parts.append(child.get(text_key, ''))
        elif child.get('type') == 'text':
            parts.append(child.get('value', ''))
        elif child.get('type') in ('inlineCode',):
            parts.append(child.get('value', ''))
        elif 'children' in child:
            parts.append(collect_text(child['children'], text_key))
    text = ' '.join(parts) if parts else ''
    return ' '.join(text.split())
