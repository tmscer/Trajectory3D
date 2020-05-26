class _Plot:

    style = 'default'

    subplot_kwargs = {
        'left': 0.1,
        'right': 0.95,
        'top': 0.95,
        'bottom': 0.06,
        'wspace': 0.15,
    }

    label_font_size = 13

    grid_kwargs = {
        'color': 'grey',
        'linewidth': 0.5,
        'linestyle': '--',
    }


class _Panel:

    large_font_family = "Helvetica"
    large_font_size = 16

    large_text = (large_font_family, large_font_size)

    width = 300


plot = _Plot()
panel = _Panel()
