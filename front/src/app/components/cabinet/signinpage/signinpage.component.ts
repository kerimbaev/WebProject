import { Component, OnInit } from '@angular/core';
import { strict } from 'assert';
import { RouterLink } from '@angular/router';
import { UserService } from '../../../services/user.service';
import {UserInterface} from '../../../database/userInterface';
@Component({
  selector: 'app-signinpage',
  templateUrl: './signinpage.component.html',
  styleUrls: ['./signinpage.component.css']
})
export class SigninpageComponent implements OnInit {
  logged = this.userService.getBl();
  isSuper: boolean;
  user: UserInterface;
  username = '';
  password = '';
  constructor(
    private userService: UserService
  ) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {

      this.logged = true;
      this.userService.setBl(true);
      this.userService.refreshh(this.logged);
    }
  }


  test(){
    alert("checking");
    this.userService.login(this.username, this.password)
    .subscribe(res => {

      localStorage.setItem('token', res.token);
      this.userService.setUsername(this.username);
      this.user = this.userService.getUser("aaa")
      this.logged = true;

      this.userService.changeDesign("logged");

      this.username = '';
      this.password = '';
      this.signin(this.username);
    });
  }
 
  
  signin(login: string){
  //Coming SOON TODO
  document.getElementById("h5Hide").style.display = "block";
  document.getElementById("h5Hide2").style.display = "block";
  document.getElementById("btnHide").style.display = "none";

  }

}
