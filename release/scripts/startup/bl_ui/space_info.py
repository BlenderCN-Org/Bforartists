﻿# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
import bpy
from bpy.types import Header, Menu

############################### Tabs to switch between layouts ###################################################

class switch_layout_to_default(bpy.types.Operator):
    """Switch to Default theme\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout Default in the dropdown list\nThis will make the button disfunctional"""     # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "wm.switch_layout_to_default"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to Default layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
 

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['Default']
        return {'FINISHED'}

class switch_layout_to_animation(bpy.types.Operator):
    """Switch to Animation layout\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout Animation in the dropdown list\nThis will make the button disfunctional"""  
    bl_idname = "wm.switch_layout_to_animation"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to Animation layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['Animation']
        return {'FINISHED'}

class switch_layout_to_uv(bpy.types.Operator):
    """Switch to UV Editing layout\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout UV Editing in the dropdown list\nThis will make the button disfunctional"""  
    bl_idname = "wm.switch_layout_to_uv"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to UV Editing layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['UV Editing']
        return {'FINISHED'}

class switch_layout_to_compositing(bpy.types.Operator):
    """Switch to Compositing layout\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout Compositing in the dropdown list\nThis will make the button disfunctional"""  
    bl_idname = "wm.switch_layout_to_compositing"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to Compositing layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['Compositing']
        return {'FINISHED'}

class switch_layout_to_scripting(bpy.types.Operator):
    """Switch to Scripting layout\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout Scripting in the dropdown list\nThis will make the button disfunctional"""  
    bl_idname = "wm.switch_layout_to_scripting"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to Scripting layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['Scripting']
        return {'FINISHED'}

class switch_layout_to_motiontracking(bpy.types.Operator):
    """Switch to Motion Tracking layout\nWARNING! This Button relies at the layouts in the layout dropdown box\nDon't rename or remove the layout Motion Tracking in the dropdown list\nThis will make the button disfunctional"""  
    bl_idname = "wm.switch_layout_to_motiontracking"        # unique identifier for buttons and menu items to reference.
    bl_label = "Switch to Motion Tracking layout"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.context.window.screen = bpy.data.screens['Motion Tracking']
        return {'FINISHED'}

###########################################################################################################

class INFO_HT_header(Header):
    bl_space_type = 'INFO'

    def draw(self, context):
        layout = self.layout

        window = context.window
        scene = context.scene
        rd = scene.render

        ALL_MT_editormenu.draw_hidden(context, layout) # bfa - show hide the editormenu
        INFO_MT_editor_menus.draw_collapsible(context, layout)

        if window.screen.show_fullscreen:
            layout.operator("screen.back_to_previous", icon='SCREEN_BACK', text="Back to Previous")
            layout.separator()
        else:
            layout.template_ID(context.window, "screen", new="screen.new", unlink="screen.delete")
           # layout.template_ID(context.screen, "scene", new="scene.new", unlink="scene.delete") # bfa - removed the scene drodpown box

        layout.separator()


        #if rd.has_multiple_engines: # bfa - removed the renderer drodpown box, and moved it to Properties editor.
        #    layout.prop(rd, "engine", text="")

        layout.separator()

        layout.template_running_jobs()

        layout.template_reports_banner()

        row = layout.row(align=True)

        if bpy.app.autoexec_fail is True and bpy.app.autoexec_fail_quiet is False:
            row.label("Auto-run disabled", icon='ERROR')
            if bpy.data.is_saved:
                props = row.operator("wm.revert_mainfile", icon='SCREEN_BACK', text="Reload Trusted")
                props.use_scripts = True

            row.operator("script.autoexec_warn_clear", text="Ignore")

            # include last so text doesn't push buttons out of the header
            row.label(bpy.app.autoexec_fail_message)
            return

        row.operator("wm.switch_layout_to_default", text="Def")
        row.operator("wm.switch_layout_to_animation", text="Ani")
        row.operator("wm.switch_layout_to_uv", text="UV")
        row.operator("wm.switch_layout_to_compositing", text="Com")
        row.operator("wm.switch_layout_to_scripting", text="Scr")
        row.operator("wm.switch_layout_to_motiontracking", text="MoT")

        row.label(text=scene.statistics(), translate=False)

# bfa - show hide the editormenu
class ALL_MT_editormenu(Menu):
    bl_label = ""

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):

        row = layout.row(align=True)
        row.template_header() # editor type menus

# --------------------------------menu items, down to line 310

class INFO_MT_editor_menus(Menu):
    bl_idname = "INFO_MT_editor_menus"
    bl_label = ""

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        scene = context.scene
        rd = scene.render

        layout.menu("INFO_MT_file")

        if rd.use_game_engine:
            layout.menu("INFO_MT_game")
        else:
            layout.menu("INFO_MT_render")

        layout.menu("INFO_MT_window")
        layout.menu("INFO_MT_help")


class INFO_MT_file(Menu):
    bl_label = "File"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.read_homefile", text="New", icon='NEW')
        layout.operator("wm.open_mainfile", text="Open...", icon='FILE_FOLDER')
        layout.menu("INFO_MT_file_open_recent", icon='OPEN_RECENT')
        layout.operator("wm.revert_mainfile", icon='FILE_REFRESH')
        layout.operator("wm.recover_last_session", icon='RECOVER_LAST')
        layout.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')

        layout.separator()

        layout.operator_context = 'EXEC_AREA' if context.blend_data.is_saved else 'INVOKE_AREA'
        layout.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save Copy...", icon='SAVE_COPY').copy = True

        layout.separator()

        layout.operator("screen.userpref_show", text="User Preferences...", icon='PREFERENCES')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_homefile", icon='SAVE_PREFS')
        layout.operator("wm.read_factory_settings", icon='LOAD_FACTORY')

        layout.separator()

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.link", text="Link", icon='LINK_BLEND')
        layout.operator("wm.append", text="Append", icon='APPEND_BLEND')
        layout.menu("INFO_MT_file_previews")

        layout.separator()

        layout.menu("INFO_MT_file_import", icon='IMPORT')
        layout.menu("INFO_MT_file_export", icon='EXPORT')

        layout.separator()

        layout.menu("INFO_MT_file_external_data", icon='EXTERNAL_DATA')

        layout.separator()

        layout.operator_context = 'EXEC_AREA'
        if bpy.data.is_dirty and context.user_preferences.view.use_quit_dialog:
            layout.operator_context = 'INVOKE_SCREEN'  # quit dialog
        layout.operator("wm.quit_blender", text="Quit", icon='QUIT')


class INFO_MT_file_import(Menu):
    bl_idname = "INFO_MT_file_import"
    bl_label = "Import"

    def draw(self, context):
        if bpy.app.build_options.collada:
            self.layout.operator("wm.collada_import", text="Collada (Default) (.dae)")


class INFO_MT_file_export(Menu):
    bl_idname = "INFO_MT_file_export"
    bl_label = "Export"

    def draw(self, context):
        if bpy.app.build_options.collada:
            self.layout.operator("wm.collada_export", text="Collada (Default) (.dae)")


class INFO_MT_file_external_data(Menu):
    bl_label = "External Data"

    def draw(self, context):
        layout = self.layout

        icon = 'CHECKBOX_HLT' if bpy.data.use_autopack else 'CHECKBOX_DEHLT'
        layout.operator("file.autopack_toggle", icon=icon)

        layout.separator()

        pack_all = layout.row()
        pack_all.operator("file.pack_all")
        pack_all.active = not bpy.data.use_autopack

        unpack_all = layout.row()
        unpack_all.operator("file.unpack_all")
        unpack_all.active = not bpy.data.use_autopack

        layout.separator()

        layout.operator("file.make_paths_relative")
        layout.operator("file.make_paths_absolute")
        layout.operator("file.report_missing_files")
        layout.operator("file.find_missing_files")



class INFO_MT_file_previews(Menu):
    bl_label = "Data Previews"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.previews_ensure")


class INFO_MT_game(Menu):
    bl_label = "Game"

    def draw(self, context):
        layout = self.layout

        gs = context.scene.game_settings

        layout.operator("view3d.game_start")

        layout.separator()

        layout.prop(gs, "show_debug_properties")
        layout.prop(gs, "show_framerate_profile")
        layout.prop(gs, "show_physics_visualization")
        layout.prop(gs, "use_deprecation_warnings")
        layout.prop(gs, "use_animation_record")
        layout.separator()
        layout.prop(gs, "use_auto_start")


class INFO_MT_render(Menu):
    bl_label = "Render"

    def draw(self, context):
        layout = self.layout

        layout.operator("render.render", text="Render Image", icon='RENDER_STILL').use_viewport = True
        props = layout.operator("render.render", text="Render Animation", icon='RENDER_ANIMATION')
        layout.operator("sound.mixdown", text="Mixdown Audio", icon='PLAY_AUDIO')
        props.animation = True
        props.use_viewport = True

        layout.separator()

        layout.operator("render.opengl", text="OpenGL Render Image")
        layout.operator("render.opengl", text="OpenGL Render Animation").animation = True
        layout.menu("INFO_MT_opengl_render")

        layout.separator()

        layout.operator("render.view_show")
        layout.operator("render.play_rendered_anim", icon='PLAY')


class INFO_MT_opengl_render(Menu):
    bl_label = "OpenGL Render Options"

    def draw(self, context):
        layout = self.layout

        rd = context.scene.render

        layout.prop(rd, "use_antialiasing")
        layout.prop_menu_enum(rd, "antialiasing_samples")
        layout.prop_menu_enum(rd, "alpha_mode")


class INFO_MT_window(Menu):
    bl_label = "Window"

    def draw(self, context):
        import sys

        layout = self.layout

        layout.operator("wm.window_duplicate")
        layout.operator("wm.window_fullscreen_toggle", icon='FULLSCREEN_ENTER')

        layout.separator()

        layout.operator("screen.screenshot")
        layout.operator("screen.screencast")

        if sys.platform[:3] == "win":
            layout.separator()
            layout.operator("wm.console_toggle", icon='CONSOLE')

        if context.scene.render.use_multiview:
            layout.separator()
            layout.operator("wm.set_stereo_3d", icon='CAMERA_STEREO')

        layout.separator()

        layout.menu("WM_OT_redraw_timer", icon='BLENDER') #Redraw timer sub menu - Debug stuff
        layout.operator("wm.debug_menu") # debug menu
        layout.operator("script.reload") # Reload all python scripts. Mainly meant for the UI scripts.

        layout.separator()

        layout.operator("wm.search_menu") # The search menu. Note that this just calls the pure search menu, and not the whole search menu addon.


class INFO_MT_help(Menu):
    bl_label = "Help"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.url_open", text="Manual", icon='HELP').url = "http://www.bforartists.de/wiki/Manual"
        layout.operator("wm.url_open", text="Release notes", icon='URL').url = "http://www.bforartists.de/wiki/release-notes"
        layout.separator()

        layout.operator("wm.url_open", text="Bforartists Website", icon='URL').url = "http://www.bforartists.de"
        layout.separator()
        layout.operator("wm.url_open", text="Report a Bug", icon='URL').url = "http://www.bforartists.de/node/add/project-issue/bforartists_bugtracker"
        layout.separator()

        layout.operator("wm.url_open", text="Python API Reference", icon='URL').url = "http://www.bforartists.de/pythonapi/contents.html"
        layout.operator("wm.sysinfo", icon='TEXT')
        layout.separator()

        layout.operator("wm.splash", icon='BLENDER')

#Redraw timer sub menu - Debug stuff
class WM_OT_redraw_timer(Menu):
    bl_label = "Redraw Timer"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.redraw_timer", text = 'Draw Region').type ='DRAW'
        layout.operator("wm.redraw_timer", text = 'Draw Region + Swap').type ='DRAW_SWAP'
        layout.operator("wm.redraw_timer", text = 'Draw Window').type ='DRAW_WIN'
        layout.operator("wm.redraw_timer", text = 'Draw Window + Swap').type ='DRAW_WIN_SWAP'
        layout.operator("wm.redraw_timer", text = 'Anim Step').type ='ANIM_STEP'
        layout.operator("wm.redraw_timer", text = 'Anim Play').type ='ANIM_PLAY'
        layout.operator("wm.redraw_timer", text = 'Undo/Redo').type ='UNDO'


if __name__ == "__main__":  # only for live edit.
    bpy.utils.register_module(__name__)
