function checkImageSize(image, defaultImageUrl) {
    if (image.naturalWidth === 1 && image.naturalHeight === 1) {
        image.src = defaultImageUrl;
    }
}