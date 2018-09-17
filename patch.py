# coding: utf-8

from recommonmark.parser import CommonMarkParser, _SectionHandler, append_inlines
from CommonMark import DocParser
from docutils import nodes


def parse(self, inputstring, document):
    self._patch_id = 0
    self.setup_parse(inputstring, document)

    self.document = document
    self.current_node = document
    self.section_handler = _SectionHandler(document)

    parser = DocParser()

    ast = parser.parse(inputstring + '\n')

    self.convert_block(ast)

    self.finish_parse()


# Blocks
def section(self, block):
    self._patch_id += 1
    new_section = nodes.section()
    new_section.line = block.start_line
    new_section['level'] = block.level

    title_node = nodes.title()
    title_node.line = block.start_line
    append_inlines(title_node, block.inline_content)
    new_section.append(title_node)
    name = nodes.fully_normalize_name(title_node.astext())
    new_section['names'].append(name)
    self.current_node.document.note_implicit_target(new_section, new_section)
    # nodes.make_id(name)
    new_section['ids'].append('id' + str(self._patch_id))

    self.section_handler.add_new_section(new_section, block.level)
    self.current_node = new_section


CommonMarkParser.parse = parse
CommonMarkParser.section = section
