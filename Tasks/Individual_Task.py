#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from dataclasses import dataclass
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod


@dataclass
class Triad(ABC):
    a: int
    b: int
    c: int

    @abstractmethod
    def increase(self) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    @classmethod
    def from_xml(cls, file: str) -> Triad:
        with open(file, 'r') as file:
            xml_string = file.read()
        root = ET.fromstring(xml_string)
        return cls(int(root.find('a').text),
                   int(root.find('b').text),
                   int(root.find('c').text))

    def to_xml(self, file: str) -> None:
        root = ET.Element('Triad')
        ET.SubElement(root, 'a').text = str(self.a)
        ET.SubElement(root, 'b').text = str(self.b)
        ET.SubElement(root, 'c').text = str(self.c)
        with open(file, 'w') as file:
            file.write(ET.tostring(root).decode('utf-8'))


@dataclass
class Date(Triad):
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        super().__init__(day, month, year)

    def increase(self) -> None:
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self) -> None:
        print(f"Дата: {self.a}/{self.b}/{self.c}")

    @classmethod
    def from_xml(cls, file: str) -> Date:
        with open(file, 'r') as file:
            string = file.read()
        root = ET.fromstring(string)
        return cls(int(root.find('day').text),
                   int(root.find('month').text), int(root.find('year').text))

    def to_xml(self, file: str) -> None:
        root = ET.Element('Date')
        ET.SubElement(root, 'day').text = str(self.a)
        ET.SubElement(root, 'month').text = str(self.b)
        ET.SubElement(root, 'year').text = str(self.c)
        with open(file, 'w') as file:
            file.write(ET.tostring(root).decode('utf-8'))


@dataclass
class Time(Triad):
    hour: int
    minute: int
    second: int

    def __init__(self, hour: int, minute: int, second: int):
        super().__init__(hour, minute, second)

    def increase(self) -> None:
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self) -> None:
        print(f"Время: {self.a}:{self.b}:{self.c}")

    @classmethod
    def from_xml(cls, file: str) -> Time:
        with open(file, 'r') as file:
            string = file.read()
        root = ET.fromstring(string)
        return cls(int(root.find('hour').text),
                   int(root.find('minute').text),
                   int(root.find('second').text))

    def to_xml(self, file: str) -> None:
        root = ET.Element('Time')
        ET.SubElement(root, 'hour').text = str(self.a)
        ET.SubElement(root, 'minute').text = str(self.b)
        ET.SubElement(root, 'second').text = str(self.c)
        with open(file, 'w') as file:
            file.write(ET.tostring(root).decode('utf-8'))


if __name__ == '__main__':
    date: Date = Date(17, 3, 2001)
    time: Time = Time(12, 30, 45)
    date.to_xml('date.xml')
    time.to_xml('time.xml')
    load_date = Date.from_xml('date.xml')
    load_time = Time.from_xml('time.xml')

    print("\nЗагруженные данные:")
    load_date.display()
    load_time.display()
