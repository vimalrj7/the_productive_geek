from __future__ import unicode_literals
from django.db import models
import datetime

helpp = """<textarea cols=100 rows=20 readonly>
<!-- Post Image Start -->
<div class="post-image margin-top-40 margin-bottom-40">
   <img src="/media/img/" alt="image" width='500px' height='500px'>
   <p>#</p>
  </div>
<!-- Post Image End -->

----------------------------------------------------------------------

 <!-- Post Video Tutorial Start -->
 <div class="video-box margin-top-40 margin-bottom-40">
  <div class="video-tutorial">
   <a class="video-popup" href="#" title="#">
   <img src="images/blog/#" alt="">
   </a>
  </div>
 <p>Integrate video on magnific popup for fast page load.</p>
</div>
<!-- Post Video Tutorial End -->

-----------------------------------------------------------------------

<!-- Post Blockquote Start -->
  <div class="post-quote margin-top-40 margin-bottom-40">
    <blockquote>#</blockquote>
  </div>
<!-- Post Blockquote End -->

-------------------------------------------------------------------------

<!-- Post Coding (SyntaxHighlighter) Start -->
  <div class="margin-top-40 margin-bottom-40">
   <pre class="brush: js">
   /* Smooth Scroll */

    $('a.smoth-scroll').on("click", function (e) {
      var anchor = $(this);
      $('html, body').stop().animate({
      scrollTop: $(anchor.attr('href')).offset().top - 50
      }, 1000);
      e.preventDefault();
     });

   /* Scroll To Top */

   $(window).scroll(function(){
     if ($(this).scrollTop() >= 500) {
     $('.scroll-to-top').fadeIn();
     } else {
     $('.scroll-to-top').fadeOut();
     }
     });

   $('.scroll-to-top').click(function(){
   $('html, body').animate({scrollTop : 0},800);
   return false;
    });
  </pre>
 </div>
<!-- Post Coding (SyntaxHighlighter) End -->

-------------------------------------------------------------------------------

<!-- Post Image Gallery Start -->
  <div class="row margin-top-40 margin-bottom-40">

    <div class="col-md-4 col-sm-6 col-xs-12">
      <a href="images/blog/7.jpg" class="image-popup" title="image Title">
      <img src="images/blog/7.jpg" class="img-responsive" alt="">
     </a>
    </div>

    <div class="col-md-4 col-sm-6 col-xs-12">
      <a href="images/blog/5.jpg" class="image-popup" title="image Title">
      <img src="images/blog/5.jpg" class="img-responsive" alt="">
     </a>
    </div>

   <div class="col-md-4 col-sm-6 col-xs-12">
     <a href="images/blog/6.jpg" class="image-popup" title="image Title">
     <img src="images/blog/6.jpg" class="img-responsive" alt="">
    </a>
   </div>

 </div>
<!-- Post Image Gallery End -->

-----------------------------------------------------------------------------------

<!-- Post Blockquote (Italic Style) Start -->
  <blockquote class="margin-top-40 margin-bottom-40">
    <p>###</p>
   </blockquote>
<!-- Post Blockquote (Italic Style) End -->

------------------------------------------------------------------------------------

<!-- Post List Style Start -->
  <div class="list">
   <ul>
     <li></li>
     <li></li>
     <li></li>
    </ul>
   </div>


  <div class="list list-style margin-top-40">
   <ul>
     <li></li>
     <li></li>
     <li></li>
    </ul>
   </div>


  <div class="list list-style-2 margin-top-40">
   <ul>
     <li></li>
     <li></li>
     <li></li>
    </ul>
   </div>
<!-- Post List Style End -->

----------------------------------------------------------------------------------------

<!-- Post Author Bio Box Start -->
  <div class="about-author margin-top-70 margin-bottom-50">

    <div class="picture">
      <img src="images/blog/author.png" class="img-responsive" alt="">
     </div>

    <div class="c-padding">
       <h3>Article By <a href="#" target="_blank" data-toggle="tooltip" data-placement="top" title="Visit Alex Website"></a></h3>
       <p>You can use about author box when someone guest post on your blog.</p>
      </div>
    </div>
<!-- Post Author Bio Box End -->
</textarea>"""

class Img(models.Model):
    post = models.ForeignKey('Post', related_name="images")
    image = models.ImageField(upload_to='img')

class Post(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    body = models.TextField(help_text=helpp)
    intro = models.TextField(null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title





