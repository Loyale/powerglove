'''
Created on Apr 24, 2012

@author: lgoff
'''
import serial

class PowerGlove(object):
    '''
    PowerGlove class for IO to 
    '''
    def __init__(self, name, com):
        '''
        Constructor
        '''
        self.name = name
        self.com = com
        self.baud = 9600
        self.bitflag=0
        self.buttons = {0: {'bit':0x01,'name':'up'},
                    1: {'bit':0x02,'name':'down'},
                    2: {'bit':0x04,'name':'left'},
                    3: {'bit':0x08,'name':'right'},
                    4: {'bit':0x10,'name':'B'},
                    5: {'bit':0x20,'name':'A'},
                    6: {'bit':0x40,'name':'up'},
                    7: {'bit':0x80,'name':'up'},
                    8: {'bit':0x100,'name':'up'},
                    9: {'bit':0x200,'name':'up'},
                    10: {'bit':0x400,'name':'up'},
                    11: {'bit':0x800,'name':'up'},
                    12: {'bit':0x1000,'name':'up'},
                    13: {'bit':0x2000,'name':'up'},
                    .
                    .
                    .
                    
                    
                    }
        self.accel = {'x':0,
                      'y':0,
                      'z',0}
        
    
    def _init_serial(self):
        self.serial = serial.Serial(com,self.baud)
        return True
    
    def _read_serial(self):
        return self.serial.readline()
    
    def update(self):
        self._read_serial()
        return
    
    def test_bit(self,bit):
        if (self.bitflag & bit) >0:
            return True
        else:
            return False
    
    def set_button_status(self):
        for i in self.buttons.keys():
            self.buttons[i]['status']
    
    '''
    def to_bin_str (self,v):
        """
        @brief return the binary representation of v as a string
        @param v an integer value
        @return the binary representation of v as a string
        """
        if v :
            return self.to_bin_str(self,v >> 1) + str (v & 1)
        else :
            return ""
    
    def get_mask (self, first_bit, flag_width ) :
        """
        @brief construct the mask of a bitfield specified by the position of the first significant bit
        and the width, in number of bits, of the flag to read
        @param first_bit position of the first significant bit
        @param flag_width number of bits, of the flag to read
        @return the mask value, as an integer matching the binary : "flag_width" number of 1 + " first_bit" number of 0"
        """
        mask = 0
        for exp in xrange( flag_width ):
            mask += 2 ** ( first_bit + exp )
        return mask
       
    def get_bitflag_by_range (self, flag_word, first_bit, flag_width ) :
        """
        @brief read the bit flag values by specifying the first bit position and the flag width
        @warning if flag_width is null, an exception is raised
        @param flag_word flag word where are stored the bits to extract
        @param flag_width the number of bits of the flag
        @return the bit flag value
        """
        if flag_width <= 0 :
            raise ValueError ( "Invalid width value %d. Must be a strictly positive integer"%flag_width )
        
        # construct the bitflag selection mask
        mask = self.get_mask(first_bit,self.flag_width )
        return self.get_bitflag_by_mask( flag_word, mask )

    def get_bitflag_by_mask (self, flag_word, mask ) :
        """
        @brief read the bit flag values by an explicit specification of the mask
        @param flag_word flag word where are stored the bits to extract
        @param mask the bits selection mask, specified as an integer
        @return the bit flag value
        """
        # find the position of the first not null bit of the mask
        first_bit_pos = self.get_first_bit_pos( mask )
        # apply a binary AND between value and mask, then shift result ot first significant bit
        return ( ( flag_word & mask ) >> first_bit_pos )
        
    def get_first_bit_pos (self, v):
        """
        @brief return the position of the first significant ( ie not null ) bit of a value, by increasing weight
        @param v an integer value
        """
        if v == 0 :
            return 0
        
        bit_pos = 0
        while ( ( v & 1 ) == 0 ) :
            bit_pos = bit_pos + 1
            v = v >> 1
        return bit_pos
    '''

class PGButton(object):
    
    def __init__(self,name,bit):
        self.name = name
        self.bit = bit
        self.depressed = False
        
    
    def __show__(self):
        return "%s: %s" % (self.name,self.depressed)
    
'''
import serial
ser = serial.Serial('/dev/tty.usbmodemfa1311',9600) #default on my system for arduino board
while 1:
    ser.readline()



'''