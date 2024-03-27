import theme_select_bar

def set_variant_selector(variant_selector):
    theme_select_bar.on_change_variant_callback = variant_selector

def get_top_bar():
    return theme_select_bar.top_bar
    
