from skeletonui_components import *
from py_tailwind_utils import *
import ofjustpy as oj
app = oj.load_app()

# ============================== alerts ==============================
oj.set_style("un")

badge_vf = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled")
badge_vf_primary = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-primary")

badge_vf_secondary = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-secondary")

badge_vf_tertiary = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-tertiary")

badge_vf_success = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-success")

badge_vf_warning = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-warning")

badge_vf_error = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-error")

badge_vf_surface = oj.PC.Span(text="Badge", extra_classes= "badge variant-filled-surface")

all_badges = [badge_vf,
              badge_vf_primary,
              badge_vf_secondary,
              badge_vf_tertiary,
              badge_vf_success,
              badge_vf_warning,
              badge_vf_error,
              badge_vf_surface
              ]

all_filled_badges_container = oj.PC.Halign(oj.PD.StackV(childs = all_badges, twsty_tags=[space/y/4, W/64, mr/st/4]))

# =========================== variant ghost ==========================
badge_vg = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost")
badge_vg_primary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-primary")

badge_vg_secondary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-secondary")

badge_vg_tertiary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-tertiary")

badge_vg_success = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-success")

badge_vg_warning = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-warning")

badge_vg_error = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-error")

badge_vg_surface = oj.PC.Span(text="Badge", extra_classes= "badge variant-ghost-surface")

all_badges = [badge_vg,
              badge_vg_primary,
              badge_vg_secondary,
              badge_vg_tertiary,
              badge_vg_success,
              badge_vg_warning,
              badge_vg_error,
              badge_vg_surface
              ]

all_ghost_badges_container = oj.PC.Halign(oj.PD.StackV(childs = all_badges, twsty_tags=[space/y/4, W/64, mr/st/4]))


# =============================== soft ===============================

badge_vs = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft")
badge_vs_primary = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-primary")

badge_vs_secondary = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-secondary")

badge_vs_tertiary = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-tertiary")

badge_vs_success = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-success")

badge_vs_warning = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-warning")

badge_vs_error = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-error")

badge_vs_surface = oj.PC.Span(text="Badge", extra_classes= "badge variant-soft-surface")

all_badges = [badge_vs,
              badge_vs_primary,
              badge_vs_secondary,
              badge_vs_tertiary,
              badge_vs_success,
              badge_vs_warning,
              badge_vs_error,
              badge_vs_surface
              ]

all_soft_badges_container = oj.PC.Halign(oj.PD.StackV(childs = all_badges, twsty_tags=[space/y/4, W/64, mr/st/4]))

# ============================== ringed ==============================
badge_vr = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed")
badge_vr_primary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-primary")

badge_vr_secondary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-secondary")

badge_vr_tertiary = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-tertiary")

badge_vr_success = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-success")

badge_vr_warning = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-warning")

badge_vr_error = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-error")

badge_vr_surface = oj.PC.Span(text="Badge", extra_classes= "badge variant-ringed-surface")

all_badges = [badge_vr,
              badge_vr_primary,
              badge_vr_secondary,
              badge_vr_tertiary,
              badge_vr_success,
              badge_vr_warning,
              badge_vr_error,
              badge_vr_surface
              ]

all_ringed_badges_container = oj.PC.Halign(oj.PD.StackV(childs = all_badges, twsty_tags=[space/y/4, W/64, mr/st/4]))


# =============================== glass ==============================
badge_vglass = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass")
badge_vglass_primary = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-primary")

badge_vglass_secondary = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-secondary")

badge_vglass_tertiary = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-tertiary")

badge_vglass_success = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-success")

badge_vglass_warning = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-warning")

badge_vglass_error = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-error")

badge_vglass_surface = oj.PC.Span(text="Badge", extra_classes= "badge variant-glass-surface")

all_badges = [badge_vglass,
              badge_vglass_primary,
              badge_vglass_secondary,
              badge_vglass_tertiary,
              badge_vglass_success,
              badge_vglass_warning,
              badge_vglass_error,
              badge_vglass_surface
              ]

all_glass_badges_container = oj.PC.Halign(oj.PD.StackV(childs = all_badges, twsty_tags=[space/y/4, W/64, mr/st/4]))




grid = oj.PD.StackG(num_cols=2,                    childs = [all_filled_badges_container,
                             all_ghost_badges_container,
                             all_soft_badges_container,
                                                             all_ringed_badges_container,
                                                             all_glass_badges_container
                             ]
             )
endpoint = oj.create_endpoint(key="td_skeleton_ui",
                   childs = [grid
                             ],
                              data_theme= 'data-theme="skeleton"',
                   title = "skeleton ui"
                   )

                   
oj.add_jproute("/", endpoint)

