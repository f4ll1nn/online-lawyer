# use Cloud Platform and Cloud Shell

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    fmts = '{:10}: {}'
    print(fmts.format('sentences', len(response.sentences)))
    print(fmts.format('tokens', len(response.tokens)))
    for token in response.tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        print(fmts.format(part_of_speech_tag.name, token.text.content))

text = 'Mum bought some fruits.'
analyze_text_syntax(text)
