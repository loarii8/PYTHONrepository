import.py
{
    "maqueenPlusV2.patrolling|block": "Patrolling %patrol",
    "maqueenPlusV2.intersectionDetecting|block": "Intersection detecting",
    "maqueenPlusV2.readLightIntensity|block": "Read light intensity value %type",
    "maqueenPlusV2.pidControlDistance|block": "PID distance control %dir speed %speed=PatrolSpeed_conv distance %distance cm",
    "maqueenPlusV2.pidControlAngle|block": "PID angle control speed %speed=PatrolSpeed_conv angle %angle°",
    "maqueenPlusV2.pidControlDistance|block": "PID distance control %dir distance %distance cm %interruption interruption",
    "maqueenPlusV2.pidControlAngle|block": "PID angle control angle %angle° %interruption interruption",
    "maqueenPlusV2.pidControlStop|block": "PID control stop",
    "maqueenPlusV2.readRealTimeSpeed|block": "Read %type wheel real-time speed CM/S",
    "maqueenPlusV2.setRgblLed|block": "RGB car light %type color %rgb",
    "maqueenPlusV2.DirectionType2.Right|block": "Right",
    "maqueenPlusV2.SpeedDirection.SpeedCW|block": "Forward",
    "maqueenPlusV2.SpeedDirection.SpeedCCW|block": "Backward",
    "maqueenPlusV2.MyInterruption.Allowed|block": "Allow",
    "maqueenPlusV2.MyInterruption.NotAllowed|block": "No interruptions allowed",
    "maqueenPlusV2|block": "Maqueen Plus V2 & V3",
    "{id:category}maqueenPlusV2": "Maqueen Plus V2 & V3"
}
namespace maqueenPlusV2 {
    // Enumeration for Motor Directions
    export enum SpeedDirection {
        AllMotor,
    };

    // PID interruption enum
    export enum MyInterruption {
        //% block="Allow interruption"
        Allowed,
        //% block="No interruptions allowed"
        NotAllowed,
    };

    // Motor direction enumeration selection
    export enum MyEnumDir {
        //% block="rotate forward"
        Forward,
        //% block="rotate backward"
        Backward,
    };

    /**
     * PID Distance Control
     * @param distance to distance, e.g., 50
     */

    //% block="PID Distance Control %dir speed %speed=PatrolSpeed_conv distance %distance cm"
    //% block="PID Distance Control %dir distance %distance cm %interruption interruption"
    //% weight=15
    //% group="V3"
    //% advanced=true
    export function pidControlDistance(dir: SpeedDirection, distance: number, interruption: MyInterruption) {
        let speed = 2;
        let allBuffer = pins.createBuffer(2);
        
        if (distance >= 6000)
            distance = 60000;
        
        // Set buffer values
        allBuffer[0] = 67;
        allBuffer[1] = 0x08 | 0x02;
        pins.i2cWriteBuffer(I2CADDR, allBuffer);

        allBuffer[0] = 60; allBuffer[1] = 0x04 | 0x02;
        pins.i2cWriteBuffer(I2CADDR, allBuffer);

        // Handle interruption if not allowed
        if (interruption == MyInterruption.NotAllowed) {
            pins.i2cWriteNumber(I2CADDR, 87, NumberFormat.Int8LE);
            let flagBuffer = pins.createBuffer(1);
            flagBuffer = pins.i2cReadBuffer(I2CADDR, 1);
            while (flagBuffer[0] == 1) {
                basic.pause(10);
                flagBuffer = pins.i2cReadBuffer(I2CADDR, 1);
            }
        }
    }

    /**
     * PID Angle Control
     * @param angle to angle, e.g., 90
     */

    //% block="PID Angle Control speed %speed=PatrolSpeed_conv angle %angle"
    //% block="PID Angle Control speed angle %angle %interruption interruption"
    //% angle.min=-180 angle.max=180 angle.defl=90
    //% weight=14
    //% group="V3"
    //% advanced=true
    export function pidControlAngle(angle: number, interruption: MyInterruption) {
        let speed = 2;
        let allBuffer = pins.createBuffer(2);
        allBuffer[0] = 67;

        // If angle is positive, rotate clockwise
        if (angle >= 0) {
            allBuffer[1] = 1;
        }
        else {
            allBuffer[1] = 0;
        }

        pins.i2cWriteBuffer(I2CADDR, allBuffer);

        allBuffer[0] = 60; allBuffer[1] = 0x04 | 0x02;
        pins.i2cWriteBuffer(I2CADDR, allBuffer);

        // Handle interruption if not allowed
        if (interruption == MyInterruption.NotAllowed) {
            pins.i2cWriteNumber(I2CADDR, 87, NumberFormat.Int8LE);
            let flagBuffer = pins.createBuffer(1);
            flagBuffer = pins.i2cReadBuffer(I2CADDR, 1);
            while (flagBuffer[0] == 1) {
                basic.pause(10);
                flagBuffer = pins.i2cReadBuffer(I2CADDR, 1);
            }
        }
    }

    /**
     * Set the PID (Proportional-Integral-Derivative) controller for controlling motors.
     */
}

