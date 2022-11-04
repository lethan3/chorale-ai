# Copyright (C) 2022 Ethan Reinart Lee. All rights reserved.
# This code is licensed under the MIT License. Please see the LICENSE file that accompanies this project for the terms of use.

from string import Template

score = Template(
"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
    <part-list>
        <score-part id="P1">
            <part-name>Piano</part-name>
            <part-abbreviation>Pno.</part-abbreviation>
            <score-instrument id="P1-I1">
                <instrument-name>Piano</instrument-name>
            </score-instrument>
            <midi-device id="P1-I1" port="1"></midi-device>
            <midi-instrument id="P1-I1">
                <midi-channel>1</midi-channel>
                <midi-program>1</midi-program>
                <volume>78.7402</volume>
                <pan>0</pan>
            </midi-instrument>
        </score-part>
    </part-list>
    <part id="P1">
        $measures
    </part>
</score-partwise>
""")

first_measure = Template(
"""<measure number="$number">
        <attributes>
            <divisions>1</divisions>
            <key>
              <fifths>$fifths</fifths>
            </key>
            <time>
                <beats>4</beats>
                <beat-type>4</beat-type>
            </time>
            <staves>2</staves>
            <clef number="1">
                <sign>G</sign>
                <line>2</line>
            </clef>
            <clef number="2">
                <sign>F</sign>
                <line>4</line>
            </clef>
        </attributes>
        <direction placement="above">
            <direction-type>
            <metronome parentheses="no" default-x="-37.68" default-y="7.12" relative-y="20.00">
                <beat-unit>quarter</beat-unit>
                <per-minute>80</per-minute>
                </metronome>
            </direction-type>
            <staff>1</staff>
            <sound tempo="80"/>
        </direction>
        $notes
    </measure>
"""
)

measure = Template(
"""<measure number="$number">
        $notes
    </measure>
"""
)

quarter_note = Template(
"""         <note>
            <pitch>
                <step>$letter</step>
                <alter>$acc</alter>
                <octave>$octave</octave>
            </pitch>
            <duration>1</duration>
            <voice>$voice</voice>
            <type>quarter</type>
            <stem>up</stem>
            <staff>$staff</staff>
        </note>
""")

backup = Template(
"""        <backup>
            <duration>1</duration>
        </backup>
"""
)

rest = Template(
"""     <measure number="$number" width="229.55">
      <note>
        <rest measure="yes"/>
        <duration>4</duration>
        <voice>1</voice>
        </note>
      </measure>
""")
