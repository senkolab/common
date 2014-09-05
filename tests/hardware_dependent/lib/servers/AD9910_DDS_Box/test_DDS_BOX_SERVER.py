"""
Tests DDS_BOX_SERVER.py module.

This testing code is specific to the case of Coach_K  being connected to
DDS Box 2 on 'COM4'

TODO: Make test code more hardware configuration independent.
"""

from twisted.trial.unittest import TestCase

import labrad
import labrad.units as _u

class Test_DDS_BOX_Server(TestCase):

    debug = False

    def setUp(self):
        """
        Connect to labrad
        """
        self.cxn = labrad.connect() #host='localhost')

        self._check_serial_server()
        # Setup default values for the camera
        self.server = self._get_tester()

        # TODO: Check that we need this
        self.server.select_device('COM4')


    def tearDown(self):
        """
        Disconnect from labrad
        """
        # Reset server values back to their default values


        self.server = None

        self.cxn.disconnect()

    def _check_serial_server(self):
        """
        Make sure the serial server is available, as this device
        depends on it.
        """

        self.assert_(hasattr(self.cxn, 'coach_k_serial_server'))


    def _get_tester(self):
        """
        Connect to DDS BOX Server.  Check that the labrad connection
        has this servers attribute.

        Returns
        -------
        cxn.avt_camera: labrad server
        """
        self.assert_(hasattr(self.cxn, 'dds_box_server'))
        return self.cxn.dds_box_server


    def test_echo(self):
        """
        Test that server has basic function echo
        """

        #server = self._get_tester()
        self.assert_(hasattr(self.server, 'echo'))



    def test_name(self):
        """
        Test server name
        """
        #server = self._get_tester()

        out = self.server.name
        exp = 'DDS Box Server'
        self.assertEquals(exp, out)


    def test_frequency_set(self):
        """
        Test setting the frequency of channel 4
        """

        server = self.server

        f = _u.WithUnit(100., 'MHz')

        server.frequency(4, f)

        out = server.frequency(4)

        exp = _u.WithUnit(100., 'MHz')


        self.assertEquals(exp, out)


















