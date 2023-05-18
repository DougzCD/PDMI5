import 'dart:async';
import 'package:flutter/material.dart';
import 'main.dart';

void main() {
  runApp(MaterialApp(
    home: SplashScreen(),
  ));
}

class SplashScreen extends StatefulWidget{
  @override
  _SplashScreenState createState() => _SplashScreenState();
}
class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Timer(Duration(seconds: 3), () {
      Navigador.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => HomeScreen()),
      );
    });
  }
}