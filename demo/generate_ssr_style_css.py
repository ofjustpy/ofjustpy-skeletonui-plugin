from svelte_bundler import build_ssr_style_css
target_module = "demo_forms_and_input"

build_ssr_style_css(target_module,
                    output_dir="./static/ssr/",
                    
                    )
