import os
import shutil
import tempfile
import unittest

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir, 'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'project': self.project,
        }
        return self.env.run(
            '%(dir)s/bin/mrbob -O %(project)s --config '
            '%(dir)s/test_answers_%(template)s.ini %(dir)s/bobtemplates/plonegovbr/%(template)s'
            % options)


class AddOnTemplateTest(BaseTemplateTest):
    """Tests for the `addon` template."""
    template = 'addon'
    project = 'brasil.gov.addon'

    def test_addon_template(self):
        """Test the `addon` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/.travis.yml',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/CHANGES.rst',
                self.project + '/CONTRIBUTORS.rst',
                self.project + '/Makefile',
                self.project + '/MANIFEST.in',
                self.project + '/README.rst',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/brasil',
                self.project + '/src/brasil/__init__.py',
                self.project + '/src/brasil/gov',
                self.project + '/src/brasil/gov/__init__.py',
                self.project + '/src/brasil/gov/addon',
                self.project + '/src/brasil/gov/addon/__init__.py',
                self.project + '/src/brasil/gov/addon/browser',
                self.project + '/src/brasil/gov/addon/browser/__init__.py',
                self.project + '/src/brasil/gov/addon/browser/configure.zcml',
                self.project + '/src/brasil/gov/addon/browser/view.py',
                self.project + '/src/brasil/gov/addon/browser/templates',
                self.project + '/src/brasil/gov/addon/browser/templates/helloworld.pt',
                self.project + '/src/brasil/gov/addon/config.py',
                self.project + '/src/brasil/gov/addon/configure.zcml',
                self.project + '/src/brasil/gov/addon/content',
                self.project + '/src/brasil/gov/addon/content/__init__.py',
                self.project + '/src/brasil/gov/addon/content/example.py',
                self.project + '/src/brasil/gov/addon/interfaces.py',
                self.project + '/src/brasil/gov/addon/profiles',
                self.project + '/src/brasil/gov/addon/profiles.zcml',
                self.project + '/src/brasil/gov/addon/profiles/default',
                self.project + '/src/brasil/gov/addon/profiles/default/browserlayer.xml',
                self.project + '/src/brasil/gov/addon/profiles/default/metadata.xml',
                self.project + '/src/brasil/gov/addon/profiles/default/rolemap.xml',
                self.project + '/src/brasil/gov/addon/profiles/default/types',
                self.project + '/src/brasil/gov/addon/profiles/default/types.xml',
                self.project + '/src/brasil/gov/addon/profiles/default/types/Example.xml',
                self.project + '/src/brasil/gov/addon/profiles/uninstall',
                self.project + '/src/brasil/gov/addon/profiles/uninstall/brasil.gov.addon.txt',
                self.project + '/src/brasil/gov/addon/static',
                self.project + '/src/brasil/gov/addon/static/document_icon.png',
                self.project + '/src/brasil/gov/addon/testing.py',
                self.project + '/src/brasil/gov/addon/tests',
                self.project + '/src/brasil/gov/addon/tests/__init__.py',
                self.project + '/src/brasil/gov/addon/tests/test_browserlayer.py',
                self.project + '/src/brasil/gov/addon/tests/test_content.py',
                self.project + '/src/brasil/gov/addon/tests/test_setup.py',
                self.project + '/src/brasil/gov/addon/upgrades',
                self.project + '/src/brasil/gov/addon/upgrades/__init__.py',
                self.project + '/src/brasil/gov/addon/upgrades/configure.zcml',
                self.project + '/src/brasil/gov/addon/upgrades/v2000',
                self.project + '/src/brasil/gov/addon/upgrades/v2000/__init__.py',
                self.project + '/src/brasil/gov/addon/upgrades/v2000/configure.zcml',
                self.project + '/src/brasil/gov/addon/upgrades/v2000/handler.py',
                self.project + '/src/brasil/gov/addon/upgrades/v2000/profile',
                self.project + '/src/brasil/gov/addon/upgrades/v2000/profile/metadata.xml',
                self.project + '/travis.cfg',
            ]
        )


class TemaTemplateTest(BaseTemplateTest):
    """Tests for the `tema` template."""
    template = 'tema'
    project = 'brasil.gov.tema'

    def test_tema_template(self):
        """Test the `tema` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/.travis.yml',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/CHANGES.rst',
                self.project + '/CONTRIBUTORS.rst',
                self.project + '/Makefile',
                self.project + '/MANIFEST.in',
                self.project + '/README.rst',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/brasil',
                self.project + '/src/brasil/__init__.py',
                self.project + '/src/brasil/gov',
                self.project + '/src/brasil/gov/__init__.py',
                self.project + '/src/brasil/gov/tema',
                self.project + '/src/brasil/gov/tema/__init__.py',
                self.project + '/src/brasil/gov/tema/config.py',
                self.project + '/src/brasil/gov/tema/configure.zcml',
                self.project + '/src/brasil/gov/tema/Extensions',
                self.project + '/src/brasil/gov/tema/Extensions/__init__.py',
                self.project + '/src/brasil/gov/tema/Extensions/Install.py',
                self.project + '/src/brasil/gov/tema/interfaces.py',
                self.project + '/src/brasil/gov/tema/profiles',
                self.project + '/src/brasil/gov/tema/profiles.zcml',
                self.project + '/src/brasil/gov/tema/profiles/default',
                self.project + '/src/brasil/gov/tema/profiles/default/browserlayer.xml',
                self.project + '/src/brasil/gov/tema/profiles/default/cssregistry.xml',
                self.project + '/src/brasil/gov/tema/profiles/default/jsregistry.xml',
                self.project + '/src/brasil/gov/tema/profiles/default/metadata.xml',
                self.project + '/src/brasil/gov/tema/profiles/default/theme.xml',
                self.project + '/src/brasil/gov/tema/profiles/uninstall',
                self.project + '/src/brasil/gov/tema/profiles/uninstall/brasil.gov.tema.txt',
                self.project + '/src/brasil/gov/tema/profiles/uninstall/theme.xml',
                self.project + '/src/brasil/gov/tema/testing.py',
                self.project + '/src/brasil/gov/tema/tests',
                self.project + '/src/brasil/gov/tema/tests/__init__.py',
                self.project + '/src/brasil/gov/tema/tests/test_browserlayer.py',
                self.project + '/src/brasil/gov/tema/tests/test_setup.py',
                self.project + '/src/brasil/gov/tema/tests/test_theme.py',
                self.project + '/src/brasil/gov/tema/themes',
                self.project + '/src/brasil/gov/tema/themes/azul',
                self.project + '/src/brasil/gov/tema/themes/azul/css',
                self.project + '/src/brasil/gov/tema/themes/azul/css/plone.css',
                self.project + '/src/brasil/gov/tema/themes/azul/css/style.css',
                self.project + '/src/brasil/gov/tema/themes/azul/img',
                self.project + '/src/brasil/gov/tema/themes/azul/img/acesso-a-infornacao.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/background_footer.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/bg-acess-key.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/bg-menu-mobile-panel.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/bg-menu-mobile.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/border-hor.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/border-ver.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/brasil.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/bullet.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/cadeado.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/carta-comentarios.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/coala.jpeg',
                self.project + '/src/brasil/gov/tema/themes/azul/img/em-destaque.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/favicon.ico',
                self.project + '/src/brasil/gov/tema/themes/azul/img/flag-en.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/flag-es.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/header.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-facebook.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-facebook.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-flickr.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-related-items.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-twitter.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/icone-youtube.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/mais_fotos.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/menu-ativo.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/menu-mobile-item.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/portlet-footer-textmore.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/portlet-header-expanded.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/portlet-header.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoreblue.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmorebrown.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoredarkblue.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoredarkgray.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoregray.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoregreen.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmoreorange.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmorepurple.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/readmorewhiteblue.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/reportar-erros.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/search-buttom.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/search-button-30px.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/search-button.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/search-ico.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/sections-ico.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_cidadania_justica.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_ciencia_tecnologia.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_cultura.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_defesa_seguranca.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_economia_emprego.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_educacao.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_esporte.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_governo.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_infraestrutura.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_meio_ambiente.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_saude.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/seta_tursimo.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/shadow-bottom.gif',
                self.project + '/src/brasil/gov/tema/themes/azul/img/sprite-icons.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/sprite-setas.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/sprite.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/touch_icon.png',
                self.project + '/src/brasil/gov/tema/themes/azul/img/voltar-topo.png',
                self.project + '/src/brasil/gov/tema/themes/azul/index.html',
                self.project + '/src/brasil/gov/tema/themes/azul/js',
                self.project + '/src/brasil/gov/tema/themes/azul/js/menu.js',
                self.project + '/src/brasil/gov/tema/themes/azul/manifest.cfg',
                self.project + '/src/brasil/gov/tema/themes/azul/preview.png',
                self.project + '/src/brasil/gov/tema/themes/azul/rules.xml',
                self.project + '/src/brasil/gov/tema/upgrades',
                self.project + '/src/brasil/gov/tema/upgrades/__init__.py',
                self.project + '/src/brasil/gov/tema/upgrades/configure.zcml',
                self.project + '/src/brasil/gov/tema/upgrades/v2000',
                self.project + '/src/brasil/gov/tema/upgrades/v2000/__init__.py',
                self.project + '/src/brasil/gov/tema/upgrades/v2000/configure.zcml',
                self.project + '/src/brasil/gov/tema/upgrades/v2000/handler.py',
                self.project + '/src/brasil/gov/tema/upgrades/v2000/profile',
                self.project + '/src/brasil/gov/tema/upgrades/v2000/profile/metadata.xml',
                self.project + '/travis.cfg',
            ]
        )
