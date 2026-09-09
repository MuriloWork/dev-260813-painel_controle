import sys
from pathlib import Path
from markdown_it import MarkdownIt

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'parse_utils'))
import string_utils


class GenerateAst:
    def get_ast_model(self):
        return {
            "type": "root",
            "children": [
                {"type": "heading", "fields": {"depth": "int", "start_line": "int", "end_line": "int"}, "children": [{"type": "text", "fields": {"start_line": "int", "end_line": "int"}}]},
                {"type": "paragraph", "children": [
                    {"type": "text", "fields": {"start_line": "int", "end_line": "int"}},
                    {"type": "strong", "children": [{"type": "text"}]},
                    {"type": "em", "children": [{"type": "text"}]},
                    {"type": "inlineCode"},
                    {"type": "link", "fields": {"url": "str", "title": "str", "start_line": "int", "end_line": "int"}, "children": [{"type": "text"}]}
                ]},
                {"type": "code", "fields": {"lang": "str", "value": "str", "start_line": "int", "end_line": "int"}},
                {"type": "list", "fields": {"ordered": "bool", "start_line": "int", "end_line": "int"}, "children": [
                    {"type": "listItem", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                        {"type": "paragraph", "children": [{"type": "text"}]}
                    ]}
                ]},
                {"type": "blockquote", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                    {"type": "paragraph", "children": [{"type": "text"}]}
                ]},
                {"type": "thematicBreak", "fields": {"start_line": "int", "end_line": "int"}},
                {"type": "table", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                    {"type": "tableRow", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                        {"type": "tableCell", "fields": {"start_line": "int", "end_line": "int"}, "children": [{"type": "text"}]}
                    ]}
                ]}
            ]
        }

    MD_TYPE_MAP = {
        'heading_open': 'heading',
        'paragraph_open': 'paragraph',
        'inline': None,
        'text': 'text',
        'code_block': 'code',
        'fence': 'code',
        'bullet_list_open': 'list',
        'ordered_list_open': 'list',
        'list_item_open': 'listItem',
        'blockquote_open': 'blockquote',
        'hr': 'thematicBreak',
        'table_open': 'table',
        'thead_open': None,
        'tbody_open': None,
        'tr_open': 'tableRow',
        'th_open': 'tableCell',
        'td_open': 'tableCell',
        'strong_open': 'strong',
        'em_open': 'em',
        'link_open': 'link',
        'code_inline': 'inlineCode',
        'image': 'image',
        'soft_break': None,
        'hard_break': 'br',
        'html_block': None,
        'html_inline': None,
    }

    PARAGRAPH_INLINE_CHILDREN = {'text', 'strong', 'em', 'inlineCode', 'link', 'br', 'image'}

    def _collect_text(self, children):
        return string_utils.collect_text(children, text_key='value')

    def parse_file(self, md_path, ast_model=None):
        with open(md_path, 'r', encoding='utf-8') as f:
            source = f.read()
        md = MarkdownIt('js-default')
        tokens = md.parse(source)
        ast = self._tokens_to_ast(tokens, ast_model)
        return ast

    def _tokens_to_ast(self, tokens, ast_model=None):
        root = {"type": "root", "children": []}
        stack = [root]
        inline_buffer = []
        heading_ctx = {}

        def attach_heading_ctx(node):
            if heading_ctx:
                node['h1'] = heading_ctx.get(1, '')
                node['h2'] = heading_ctx.get(2, '')
                node['h3'] = heading_ctx.get(3, '')
                node['h4'] = heading_ctx.get(4, '')
                node['h5'] = heading_ctx.get(5, '')
                node['h6'] = heading_ctx.get(6, '')

        def flush_inline(parent):
            if inline_buffer:
                parent['children'] = inline_buffer.copy()
                inline_buffer.clear()

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.type in ('text', 'code_inline', 'soft_break', 'hard_break'):
                node = {"type": self.MD_TYPE_MAP.get(token.type, token.type)}
                if token.type == 'code_inline':
                    node['value'] = token.content
                elif token.type == 'text':
                    node['value'] = token.content
                if token.map:
                    node['start_line'] = token.map[0]
                    node['end_line'] = token.map[1]
                inline_buffer.append(node)
                i += 1
                continue

            if token.type in ('inline',):
                if token.children:
                    sub_tokens = token.children
                    j = 0
                    while j < len(sub_tokens):
                        st = sub_tokens[j]
                        if st.type in ('text', 'code_inline', 'hard_break'):
                            node = {"type": self.MD_TYPE_MAP.get(st.type, st.type)}
                            if st.type == 'code_inline':
                                node['value'] = st.content
                            elif st.type == 'text':
                                node['value'] = st.content
                            if st.map:
                                node['start_line'] = st.map[0]
                                node['end_line'] = st.map[1]
                            inline_buffer.append(node)
                            j += 1
                        elif st.type in ('strong_open', 'em_open', 'link_open'):
                            container_type = self.MD_TYPE_MAP.get(st.type, st.type.replace('_open', ''))
                            container = {"type": container_type}
                            if st.type == 'link_open':
                                for attr in st.attrs:
                                    if attr[0] == 'href':
                                        container['url'] = attr[1]
                                    elif attr[0] == 'title':
                                        container['title'] = attr[1]
                            if st.map:
                                container['start_line'] = st.map[0]
                                container['end_line'] = st.map[1]
                            container['children'] = []
                            close_type = st.type.replace('_open', '_close')
                            j += 1
                            while j < len(sub_tokens) and sub_tokens[j].type != close_type:
                                inner_st = sub_tokens[j]
                                if inner_st.type == 'text':
                                    container['children'].append({"type": "text", "value": inner_st.content})
                                elif inner_st.type == 'code_inline':
                                    container['children'].append({"type": "inlineCode", "value": inner_st.content})
                                j += 1
                            j += 1
                            inline_buffer.append(container)
                        elif st.type in ('image',):
                            img = {"type": "image"}
                            for attr in st.attrs:
                                if attr[0] == 'src':
                                    img['url'] = attr[1]
                                elif attr[0] == 'alt':
                                    img['alt'] = attr[1]
                                elif attr[0] == 'title':
                                    img['title'] = attr[1]
                            inline_buffer.append(img)
                            j += 1
                        else:
                            j += 1
                i += 1
                continue

            if token.nesting == 1:
                container_type = self.MD_TYPE_MAP.get(token.type, token.type)
                container = {"type": container_type}
                if token.type == 'ordered_list_open':
                    container['ordered'] = True
                elif token.type == 'bullet_list_open':
                    container['ordered'] = False
                if token.type == 'fence':
                    container['type'] = 'code'
                    container['lang'] = token.info.strip() if token.info else ''
                    container['value'] = token.content
                    if token.map:
                        container['start_line'] = token.map[0]
                        container['end_line'] = token.map[1]
                if token.map:
                    container['start_line'] = token.map[0]
                    container['end_line'] = token.map[1]
                if token.type == 'code_block':
                    container['type'] = 'code'
                    container['lang'] = ''
                    container['value'] = token.content
                    if token.map:
                        container['start_line'] = token.map[0]
                        container['end_line'] = token.map[1]

                container['children'] = []
                if container_type in ('heading',):
                    depth = int(token.tag[1]) if token.tag and token.tag[0] == 'h' else 1
                    container['depth'] = depth
                    if i + 1 < len(tokens) and tokens[i + 1].type == 'inline':
                        inline_tok = tokens[i + 1]
                        if inline_tok.children:
                            container['text'] = ''.join(
                                st.content for st in inline_tok.children
                                if st.type in ('text', 'code_inline')
                            ).strip()
                        else:
                            container['text'] = inline_tok.content.strip()
                    heading_ctx[depth] = container.get('text', '')
                    for d in range(depth + 1, 7):
                        heading_ctx.pop(d, None)

                attach_heading_ctx(container)
                if container_type in ('heading', 'paragraph', 'listItem', 'tableCell'):
                    stack[-1]['children'].append(container)
                    stack.append(container)
                    inline_buffer = []
                elif container_type in ('list', 'blockquote', 'table', 'tableRow'):
                    stack[-1]['children'].append(container)
                    stack.append(container)
                i += 1

            elif token.nesting == -1:
                if token.type.endswith('_close'):
                    open_type = token.type.replace('_close', '_open')
                    close_type = self.MD_TYPE_MAP.get(open_type, token.type.replace('_close', ''))
                else:
                    close_type = self.MD_TYPE_MAP.get(token.type, token.type)
                if close_type in ('heading', 'paragraph', 'list', 'listItem', 'blockquote', 'tableRow', 'tableCell'):
                    if stack and stack[-1].get('type') == close_type:
                        if close_type in ('heading', 'paragraph', 'listItem') and inline_buffer:
                            stack[-1]['children'] = inline_buffer.copy()
                            inline_buffer = []
                        elif close_type == 'tableCell' and inline_buffer:
                            stack[-1]['children'] = inline_buffer.copy()
                            inline_buffer = []
                        stack.pop()
                elif close_type in ('table', 'list'):
                    if stack and stack[-1].get('type') == close_type:
                        stack.pop()
                i += 1

            elif token.nesting == 0:
                if token.type == 'hr':
                    node = {"type": "thematicBreak"}
                    if token.map:
                        node['start_line'] = token.map[0]
                        node['end_line'] = token.map[1]
                    attach_heading_ctx(node)
                    stack[-1]['children'].append(node)
                elif token.type == 'fence':
                    node = {"type": "code", "lang": token.info.strip() if token.info else '', "value": token.content}
                    if token.map:
                        node['start_line'] = token.map[0]
                        node['end_line'] = token.map[1]
                    attach_heading_ctx(node)
                    stack[-1]['children'].append(node)
                elif token.type == 'code_block':
                    node = {"type": "code", "lang": '', "value": token.content}
                    if token.map:
                        node['start_line'] = token.map[0]
                        node['end_line'] = token.map[1]
                    attach_heading_ctx(node)
                    stack[-1]['children'].append(node)
                elif token.type in ('th_open', 'td_open'):
                    cell_type = self.MD_TYPE_MAP.get(token.type, 'tableCell')
                    cell = {"type": cell_type}
                    if token.map:
                        cell['start_line'] = token.map[0]
                        cell['end_line'] = token.map[1]
                    stack[-1]['children'].append(cell)
                    stack.append(cell)
                    inline_buffer = []
                elif token.type in ('th_close', 'td_close'):
                    if stack and stack[-1].get('type') == 'tableCell':
                        if inline_buffer:
                            stack[-1]['children'] = inline_buffer.copy()
                            inline_buffer = []
                        stack.pop()
                i += 1
                continue

        return root

    def build_entry(self, md_path, ast, project_name, version, root_dir):
        md_path = Path(md_path)
        root_dir = Path(root_dir)
        try:
            file_path = str(md_path.relative_to(root_dir))
        except ValueError:
            file_path = md_path.name
        folder_path = str(md_path.parent)
        return {
            'project_name': project_name,
            'version': version,
            'folder_path': folder_path,
            'file_path': file_path,
            'ast': ast,
        }
