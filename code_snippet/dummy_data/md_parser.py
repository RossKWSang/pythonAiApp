from bs4 import BeautifulSoup


def parse_document(document):
    """
    Parse the document to extract summary text and text below the details tag
    :param document: HTML document string
    :return: list of tuples containing summary text and text below details tag
    """
    soup = BeautifulSoup(document, 'html.parser')
    details_tags = soup.find_all('details')

    details_data = []
    for details_tag in details_tags:
        # Extract summary text
        summary_tag = details_tag.find('summary')
        summary_text = summary_tag.get_text() if summary_tag else None

        # Extract text below details tag
        text_below_details = ''
        for element in details_tag.find_all_next():
            if element.name == 'details':
                break
            if element.name == 'summary':
                continue
            text_below_details += str(element)

        details_data.append((summary_text, text_below_details))

    return details_data
