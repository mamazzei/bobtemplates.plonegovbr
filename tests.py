import unittest2 as unittest
import os
import tempfile
import shutil

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
            '%(dir)s/test_answers.ini %(dir)s/bobtemplates/plonegovbr/%(template)s'
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
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/README.rst',
                self.project + '/src',
                self.project + '/src/brasil',
                self.project + '/src/brasil/__init__.py',
                self.project + '/src/brasil/gov',
                self.project + '/src/brasil/gov/__init__.py',
                self.project + '/src/brasil/gov/addon',
                self.project + '/src/brasil/gov/addon/__init__.py',
                self.project + '/src/brasil/gov/addon/profiles',
                self.project + '/src/brasil/gov/addon/profiles/default',
                self.project + '/src/brasil/gov/addon/profiles/default/metadata.xml',
                self.project + '/src/brasil/gov/addon/tests',
                self.project + '/src/brasil/gov/addon/tests/__init__.py',
                self.project + '/src/brasil/gov/addon/buildout.cfg',
                self.project + '/src/brasil/gov/addon/setup.py',
            ]
        )
