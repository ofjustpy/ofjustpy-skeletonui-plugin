import ofjustpy as oj
from py_tailwind_utils import *
import theme_bar_wrapper
from html_writer.macro_module import macros, writer_ctx


# <section class="w-full text-token card p-4 space-y-4">
# 					<p class="font-bold">Unordered List</p>
# 					<ul class="list">
# 						{#each listData as v}
# 							<li>
# 								<Avatar src={getImageLink({ id: v.avatar, w: 48, h: 48 })} width="w-12" />
# 								<span class="flex-auto">{v.name}</span>
# 								<span>⋮</span>
# 							</li>
# 						{/each}
# 					</ul>

with writer_ctx:
    
    with Mutable_Section(key="unordered_list", classes="w-full p-4 space-y-4", extra_classes="card text-token variant-filled-tertiary") as ul_box:
        with Prose(classes="font-bold", text="Unordered List"):
            pass
        with Ul(extra_classes="list", classes="w-96 space-y-2"):
            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Lisa Hayes"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Erin Gusikowski"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Melanie Heller"):
                        pass
                with Span(inner_html="⋮"):
                    pass                                

ul_box_section = oj.HCCMutable.Subsubsection("Unordered list",
          oj.Halign(ul_box, content_type="mutable"
                                 ),
          )                                                                    

# =========================== ordered list ===========================
# <div class="w-full text-token card p-4 space-y-4">
# 						<ol class="list">
# 							{#each listData as v, i}
# 								<li>
# 									<span class="badge-icon p-4 variant-soft-primary">{i + 1}</span>
# 									<span class="flex-auto">
# 										Numbered Item {v.label}
# 									</span>
# 									<span>⋮</span>
# 								</li>
# 							{/each}
# 						</ol>
# 					</div>


with writer_ctx:
    with Mutable_Div(key="ordered_list", classes="w-full p-4 space-y-4", extra_classes="card text-token variant-filled-tertiary") as ordered_list_box:
        with Prose(classes="font-bold", text="Ordered List"):
            pass
        with Ol(classes="w-96 space-y-2", extra_classes="list"):
            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="1"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item A"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="2"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item B"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center", extra_classes="variant-filled-surface"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="3"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item C"):
                        pass
                with Span(inner_html="⋮"):
                    pass                                

ol_box_section = oj.HCCMutable.Subsubsection("Ordered list",
          oj.Halign(ordered_list_box, content_type="mutable"
                                 ),
          )
# ========================= description list =========================

# <div class="w-full text-token card p-4 space-y-4">
# 						<dl class="list-dl">
# 							{#each listData as v}
# 								<div>
# 									<span class="badge-icon p-4 variant-soft-secondary"><i class="fa-solid fa-book" /></span>
# 									<span class="flex-auto">
# 										<dt class="font-bold">Item {v.label}</dt>
# 										<dd class="text-sm opacity-50">Description for {v.label}</dd>
# 									</span>
# 									<span>⋮</span>
# 								</div>
# 							{/each}
# 						</dl>
# 					</div>
                                                            

with writer_ctx:
    with Mutable_Div(key="desc_list", classes="w-full p-4 space-y-4", extra_classes="text-token card variant-filled-tertiary") as dl_box:
        with Prose(classes="font-bold", text="Description List"):
            pass
        
        with Dl(extra_classes="list-dl w-96 space-y-2"):
            with Li(classes="flex justify-between items-center", extra_classes="variant-filled-surface"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(classes="p-4", extra_classes="badge-icon variant-soft-secondary"):
                        with FontAwesomeIcon(label="faBook"):
                            pass
                        pass
                    with Span(classes="flex-auto"):
                        with Dt(classes="font-bold", text= "Item A"):
                            pass
                        with Dd(classes="text-sm opacity-50", text="Description for Item A"):
                            pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-surface "):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(classes="p-4", extra_classes="badge-icon variant-soft-secondary"):
                        with FontAwesomeIcon(label="faBook"):
                            pass
                        pass
                    with Span(classes="flex-auto"):
                        with Dt(classes="font-bold", text= "Item A"):
                            pass
                        with Dd(classes="text-sm opacity-50", text="Description for Item A"):
                            pass
                with Span(inner_html="⋮"):
                    pass

                
dl_box_section = oj.HCCMutable.Subsubsection("Description list",
                                             oj.Halign(dl_box, content_type="mutable"
                                                       ),
                                             )
# ============================= nav list =============================
# <div class="w-full text-token card p-4 space-y-4">
# 						<nav class="list-nav">
# 							<ul>
# 								{#each listData as v}
# 									<li>
# 										<a href="/elements/lists">
# 											<span class="badge-icon p-4 variant-soft-tertiary"><i class="fa-solid fa-arrow-right" /></span>
# 											<span class="flex-auto">
# 												Nav Item {v.label}
# 											</span>
# 											<span>⋮</span>
# 										</a>
# 									</li>
# 								{/each}
# 							</ul>
# 						</nav>


with writer_ctx:
    with Mutable_Div(key="nav-box", classes="w-full p-4 space-y-4", extra_classes="card text-token variant-filled-tertiary") as nav_box:
        with Prose(classes="font-bold", text="Navigation List"):
            pass

        with Nav("w-full"):
            with Ul(extra_classes="list", classes="w-96 space-y-2"):
                with Li(classes="flex justify-between items-center ", extra_classes=" variant-filled-surface m-2"):
                    with A(href="#"):
                        with Span(classes="flex-auto p-4 space-x-2", extra_classes="badge-icon "):
                            with FontAwesomeIcon(label="faArrowRight"):
                                pass
                            with Span(classes="flex-auto", text="Nav Item A"):
                                pass
                    with Span(inner_html="⋮"):
                        pass
                with Li(classes="flex justify-between items-center ", extra_classes=" variant-filled-surface m-2"):
                    with A(href="#"):
                        with Span(classes="flex-auto p-4 space-x-2", extra_classes="badge-icon"):
                            with FontAwesomeIcon(label="faArrowRight"):
                                pass
                            with Span(classes="flex-auto", text="Nav Item A"):
                                pass
                    with Span(inner_html="⋮"):
                        pass
                        

                    pass
                pass
            pass
        pass
    pass

nav_box_section = oj.HCCMutable.Subsubsection("Navigation list",
                                             oj.Halign(nav_box, content_type="mutable"
                                                       ),
                                             )                    


            
        
        
                                                                    
def variant_selector(dbref, msg, to_ms):
    ul_box_ms = to_ms(ul_box)
    ul_box_ms.update_extra_classes(f"card text-token {msg.value}")
    to_ms(ordered_list_box).update_extra_classes(f"card text-token {msg.value}")

    to_ms(dl_box).update_extra_classes(f"text-token card {msg.value}")
    to_ms(nav_box).update_extra_classes(f"text-token card {msg.value}")


    pass

top_bar = theme_bar_wrapper.get_top_bar()
theme_bar_wrapper.set_variant_selector(variant_selector)

tlc = oj.HCCMutable.Container(key="container", childs = [ul_box_section,
                                                         ol_box_section,
                                                         dl_box_section,
                                                         nav_box_section
                                                         ],
                              twsty_tags=[space/y/6, mr/x/auto]
                      
                      )

wp_endpoint = oj.create_endpoint(key="lists",
                                 childs = [top_bar, oj.PD.Br(twsty_tags= [mr/st/4, W/full, H/4, mr/sb/4]),
                                           tlc

                                           ],
                                 
                                 title="Lists"
                                 )
oj.add_jproute("/", wp_endpoint)
                
