def imsave(fname, arr, plugin=None, check_contrast=True, **plugin_args):
    """Save an image to file.
    Parameters
    ----------
    fname : str
        Target filename.
    arr : ndarray of shape (M,N) or (M,N,3) or (M,N,4)
        Image data.
    plugin : str, optional
        Name of plugin to use.  By default, the different plugins are
        tried (starting with imageio) until a suitable
        candidate is found.  If not given and fname is a tiff file, the
        tifffile plugin will be used.
    check_contrast : bool, optional
        Check for low contrast and print warning (default: True).
    Other Parameters
    ----------------
    plugin_args : keywords
        Passed to the given plugin.
    Notes
    -----
    When saving a JPEG, the compression ratio may be controlled using the
    ``quality`` keyword argument which is an integer with values in [1, 100]
    where 1 is worst quality and smallest file size, and 100 is best quality
    and largest file size (default 75).  This is only available when using
    the PIL and imageio plugins.
    """
    if plugin is None and hasattr(fname, 'lower'):
        if fname.lower().endswith(('.tiff', '.tif')):
            plugin = 'tifffile'
    if arr.dtype == bool:
        warn('%s is a boolean image: setting True to 255 and False to 0. '
             'To silence this warning, please convert the image using '
             'img_as_ubyte.' % fname, stacklevel=2)
        arr = arr.astype('uint8') * 255
    if check_contrast and is_low_contrast(arr):
        warn('%s is a low contrast image' % fname)
    return call_plugin('imsave', fname, arr, plugin=plugin, **plugin_args)
