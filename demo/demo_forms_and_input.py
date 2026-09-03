import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
from py_tailwind_utils import *

## the html
# <form class="w-full max-w-md mx-auto space-y-4">
# 	<fieldset class="fieldset space-y-2">
# 		<legend class="legend">Account Details</legend>
# 		<label class="label">
# 			<span class="label-text">Email</span>
# 			<input class="input" type="email" placeholder="you@example.com" />
# 		</label>
# 		<label class="label">
# 			<span class="label-text">Password</span>
# 			<input class="input" type="password" placeholder="••••••••" />
# 		</label>
# 	</fieldset>
# </form>


with MuCtx:
    # Form Container Block
    with kv.PD.Form(classes="w-full mx-auto space-y-4 max-w-md", extra_classes="") as account_form:
        
        # Fieldset Container Block
        with kv.PD.Fieldset(classes=" space-y-2", extra_classes="fieldset"):
            
            # Legend Header
            with kv.PD.Legend(extra_classes="legend"):
                with kv.PD.Prose(text="Account Details"):
                    pass
            
            # Email Input Field Block
            with kv.PD.Label(extra_classes="label"):
                with kv.PD.Span(extra_classes="label-text"):
                    with kv.PD.Prose(text="Email"):
                        pass
                with kv.PD.Input(
                        extra_classes="input",
                    type="email",
                    placeholder="you@example.com",
                    key="account_email_input"
                ):
                    pass
            
            # Password Input Field Block
            with kv.PD.Label(extra_classes="label"):
                with kv.PD.Span(extra_classes="label-text"):
                    with kv.PD.Prose(text="Password"):
                        pass
                with kv.PD.Input(
                        extra_classes="input",
                    type="password",
                    placeholder="••••••••",
                    key="account_password_input"
                ):
                    pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[account_form],
    skeleton_data_theme="mint",
    svelte_bundle_dir="ssr",
    rendering_type="SSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)
