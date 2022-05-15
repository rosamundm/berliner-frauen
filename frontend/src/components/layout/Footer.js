import React, { Component } from "react";

function Footer() {
  return (
    <div className="contact-copyright" class="py-10 font-sans text-center fixed bottom-0">
      <p>© Rosamund Mather {(new Date().getFullYear())}</p>
    </div>
 )
}

export default Footer;