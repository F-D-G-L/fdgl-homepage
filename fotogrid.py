# Provide a simple responsive fotogrid using flex layout.
# Depends on the css/fotogrid.css defined styles.
def fotogrid(image_urls):
    result = '<div class="fotorow">'
    cols = 4
    images = divmod(len(image_urls), cols)
    images_per_col = images[0]
    if images[1] > 0:
        images_per_col += 1
    nbr = 0
    for img in image_urls:
        if (nbr % images_per_col) == 0:
            if nbr > 0:
                result += '</div>'  # closing fotocolumn
            result += '<div class="fotocolumn">'
        result += '<img src="' + img + '" style="width:100%">'
        nbr += 1

    result += "</div></div>"  # closing fotocolum, fotorow
    return result