# HTML CSS


## HTML


**HTML4 Organizaion**

```
<div class="header">
<div class="nav">
<div class="section">
<div class="footer">
```

**HTML5 Organizaion**
```
<header>
<nav>
<section>
<footer>
```

** New HTML5 elements **
```
- <audio>
- <video>
- <datalist>
```


## CSS

CSS Selectors

- **_a, b_** MulIple Element Selector
- **_a b_** Descendant Selector
- **_a > b_** Child Selector i.e `ol > li { color: red; }`  red applied to li only imediate after ol and ignore anything else.
- **_a + b_** Adjacent Sibling Selector
- **_[a=b]_** AQribute Selector
- **_a:b_** Pseudoclass Selector
- **_a::b_** Pseudoelement Selector



## Responsive Design

- viewport
- Media Queries
- Flexbox
- Grids

## Nesting scss
scss
```
div {
	font-size: 18px;

	p {
		color: blue;
	}

	ul {
		color:green;
	}
}
```
 to css
 ```
div     { font-size: 18px; }

div p 	{ color: blue;     }

div ul  { color:green;     }
 ```

 **_Inheritance in SCSS_**

 