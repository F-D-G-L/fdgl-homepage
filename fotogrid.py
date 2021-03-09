# SPDX-License-Identifier: GPL-3.0


def fotogrid(image_urls):
    """
    Provide a simple responsive fotogrid using flex layout.
    Depends on the css/fotogrid.css defined styles.
    Use jinja {{ fotogrid([....]) }} from templates (registered in app.py)
    """
    if len(image_urls) == 0:
        return ""

    # prepare our 'bins', the columsn of the fotogrid
    nbr_of_columns = 4
    prepared_column = []
    for i in range(nbr_of_columns):
        prepared_column.append([])
    # sort given image URL into bins
    for i in range(len(image_urls)):
        prepared_column[i % nbr_of_columns].append(image_urls[i])

    # form HTML div structure from prepared bins
    html = '<div class="fotorow">'
    for column in prepared_column:
        if len(column) > 0:
            html += '<div class="fotocolumn">'
            for url in column:
                html += '<img src="' + url + '" style="width:100%">'
            html += "</div>"  # closing fotocolumn
    html += "</div>"  # closing fotorow

    return html
