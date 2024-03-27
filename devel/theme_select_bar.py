import ofjustpy as oj
from py_tailwind_utils import *
import macropy.activate
from hui_components import Base, BaseGroup

app = oj.load_app()
oj.set_style("un")

# ======================= top bar  select theme ======================
async def on_theme_select(dbref, msg, to_ms):
    await msg.page.run_javascript(f"""
    console.log("start setting ");
    const body = document.querySelector('body');
    console.log(body);
    body.setAttribute('data-theme', '{msg.value}');
    console.log("Done setting ");
    """)
    pass

select_theme_box  = Base("theme-selector", "Select Theme", on_change=on_theme_select)
select_theme_box.add_option('skeleton', 'skeleton')
select_theme_box.add_option('modern', 'modern')
select_theme_box.add_option('wintry', 'wintry')

select_theme_box.add_option('rocket', 'rocket')
select_theme_box.add_option('seafoam', 'seafoam')
select_theme_box.add_option('vintage', 'vintage')
select_theme_box.add_option('sahara', 'sahara')
select_theme_box.add_option('crimsom', 'crimson')


on_change_variant_callback = None
def on_change_variant_click(dbref, msg, to_ms):
    print ("variant selector clicked:", msg.value)
    if on_change_variant_callback:
        on_change_variant_callback(dbref, msg, to_ms)
        
    pass



select_variant_box  = BaseGroup("variant-selector", "Select Variant", on_change=on_change_variant_click)
filled_group = select_variant_box.add_optgroup("variant-filled")
filled_group.add_option("variant-filled", "variant-filled")
filled_group.add_option("variant-filled-primary", "primary")
filled_group.add_option("variant-filled-secondary", "secondary")
filled_group.add_option("variant-filled-tertiary", "tertiary")
filled_group.add_option("variant-filled-success", "success")
filled_group.add_option("variant-filled-warning", "warning")
filled_group.add_option("variant-filled-error", "error")
filled_group.add_option("variant-filled-surface", "surface")

ghost_group = select_variant_box.add_optgroup("variant-ghost")
ghost_group.add_option("variant-ghost", "variant-ghost")
ghost_group.add_option("variant-ghost-primary", "primary")
ghost_group.add_option("variant-ghost-secondary", "secondary")
ghost_group.add_option("variant-ghost-tertiary", "tertiary")
ghost_group.add_option("variant-ghost-success", "success")
ghost_group.add_option("variant-ghost-warning", "warning")
ghost_group.add_option("variant-ghost-error", "error")
ghost_group.add_option("variant-ghost-surface", "surface")

soft_group = select_variant_box.add_optgroup("variant-soft")
soft_group.add_option("variant-soft", "variant-soft")
soft_group.add_option("variant-soft-primary", "primary")
soft_group.add_option("variant-soft-secondary", "secondary")
soft_group.add_option("variant-soft-tertiary", "tertiary")
soft_group.add_option("variant-soft-success", "success")
soft_group.add_option("variant-soft-warning", "warning")
soft_group.add_option("variant-soft-error", "error")
soft_group.add_option("variant-soft-surface", "surface")

ringed_group = select_variant_box.add_optgroup("variant-ringed")
ringed_group.add_option("variant-ringed", "variant-ringed")
ringed_group.add_option("variant-ringed-primary", "primary")
ringed_group.add_option("variant-ringed-secondary", "secondary")
ringed_group.add_option("variant-ringed-tertiary", "tertiary")
ringed_group.add_option("variant-ringed-success", "success")
ringed_group.add_option("variant-ringed-warning", "warning")
ringed_group.add_option("variant-ringed-error", "error")
ringed_group.add_option("variant-ringed-surface", "surface")

glass_group = select_variant_box.add_optgroup("variant-glass")
glass_group.add_option("variant-glass", "variant-glass")
glass_group.add_option("variant-glass-primary", "primary")
glass_group.add_option("variant-glass-secondary", "secondary")
glass_group.add_option("variant-glass-tertiary", "tertiary")
glass_group.add_option("variant-glass-success", "success")
glass_group.add_option("variant-glass-warning", "warning")
glass_group.add_option("variant-glass-error", "error")
glass_group.add_option("variant-glass-surface", "surface")



top_bar = oj.PD.Div(twsty_tags=[W/full, db.f,  flx.rrow, space/x/4],
          childs=[select_theme_box, select_variant_box]
    )
