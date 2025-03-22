#include <Microbit_Sound.h>
#include <DFRobot_MaqueenPlusV2.h>

// Dynamic variables
volatile float mind_n_distanca, mind_n_distanca2;

// Create an object for sound
Microbit_Sound MSound;

// Create an object for the MaqueenPlus robot
DFRobot_MaqueenPlusV2 maqueenPlus;

void setup() {
    maqueenPlus.begin(15, 4);
    while (!(Button_A.isPressed() && !Button_B.isPressed())) { yield(); }
    
    maqueenPlus.setRangeColor(0, 1, 0xFF0000);
    maqueenPlus.setRangeColor(2, 3, 0x00FF00);
    
    mind_n_distanca = maqueenPlus.getDistanceCM(13, 14);
    while (mind_n_distanca <= 6 && mind_n_distanca > 0) {
        mind_n_distanca = maqueenPlus.getDistanceCM(13, 14);
        
        if (maqueenPlus.readPatrol(maqueenPlus.M) && maqueenPlus.readPatrol(maqueenPlus.L1)) {
            maqueenPlus.motorRun(maqueenPlus.ALL, maqueenPlus.CW, 255);
        } else if (maqueenPlus.readPatrol(maqueenPlus.M) && !maqueenPlus.readPatrol(maqueenPlus.L1)) {
            maqueenPlus.motorRun(maqueenPlus.LEFT, maqueenPlus.CW, 255);
            maqueenPlus.motorStop(maqueenPlus.RIGHT);
        } else if (!maqueenPlus.readPatrol(maqueenPlus.M) && maqueenPlus.readPatrol(maqueenPlus.L1)) {
            maqueenPlus.motorStop(maqueenPlus.LEFT);
            maqueenPlus.motorRun(maqueenPlus.RIGHT, maqueenPlus.CW, 255);
        } else if (maqueenPlus.readPatrol(maqueenPlus.L1) && maqueenPlus.readPatrol(maqueenPlus.M) && maqueenPlus.readPatrol(maqueenPlus.R1)) {
            maqueenPlus.motorRun(maqueenPlus.LEFT, maqueenPlus.CW, 255);
            maqueenPlus.motorRun(maqueenPlus.RIGHT, maqueenPlus.CCW, 255);
        }
        
        yield();
    }

    maqueenPlus.motorStop(maqueenPlus.ALL);
    maqueenPlus.clear();
    delay(1000);
    
    maqueenPlus.setRGB(maqueenPlus.ALL, maqueenPlus.ON);
    mind_n_distanca2 = maqueenPlus.getDistanceCM(13, 14);
    
    while (mind_n_distanca2 < 10 && mind_n_distanca2 > 0) {
        mind_n_distanca2 = maqueenPlus.getDistanceCM(13, 14);
        yield();
    }

    maqueenPlus.clear();
    maqueenPlus.motorStop(maqueenPlus.ALL);
    maqueenPlus.setRGB(maqueenPlus.ALL, maqueenPlus.OFF);
    
    MSound.play(0, RINGTONE, OnceInBackground);
    delay(1000);
    MSound.stopBackgroundPlay();
}

void loop() {
    // Empty loop
}
