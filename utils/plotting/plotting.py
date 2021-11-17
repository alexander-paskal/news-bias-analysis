"""
Contains utility functions for creating graphs, charts and figures
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def _show_figure(fn):
    """
    Decorator allowing functions accepting an axes object
    to display that object in the null case
    :return:
    :rtype:
    """
    def inner(*args, ax=None, **kwargs):
        fig = None
        if ax is None:
            fig, ax = plt.subplots()
        fn(*args, ax=ax, **kwargs)
        if fig is not None:
            plt.show()
    return inner


@_show_figure
def box_and_whisker(data, ax, ylabel=None, **kwargs):
    """
    Creates a box and whisker plot of datapoints

    :param datapoints:
    :type datapoints: Sequence
    :return:
    :rtype:
    """
    ax.boxplot(data, **kwargs)
    if ylabel:
        ax.set_ylabel(ylabel)


def bar(categories, counts):
    """
    Creates a barchart
    :param categories:
    :type categories:
    :param counts:
    :type counts:
    :return:
    :rtype:
    """
    # TODO implement bar


@_show_figure
def wordcloud(text, ax, **kwargs):
    """
    Called to create a wordcloud.
    Can either be used to generate the plot directly (default)
    or be used to affect an axes object
    :param text:
    :type text:
    :param save_to:
    :type save_to:
    :param ax:
    :type ax:
    :return:
    :rtype:
    """
    assert isinstance(text, str)

    wordcloud = WordCloud(**kwargs).generate(text)
    ax.imshow(wordcloud)


if __name__ == '__main__':
    cnn_text = """In a troubling sign that Covid is still disrupting the economy, the new jobs report indicates that US employers added only 194,000 jobs in September. 
September marked the second-straight month in which the US economy added far fewer jobs than expected. Jobs growth slowed down dramatically in August.
The unemployment rate declined to 4.8% in September, the Bureau of Labor Statistics said Friday, down from 5.2% in August. Joblessness declined across the board, with the Black unemployment rate falling the most of any group -- to 7.9% from 8.8% in August.
Biden cited those statistics in trying to put a positive spin on the report.
"Today's report has the unemployment rate down to 4.8%, a significant improvement from when I took office and a sign that our recovery is moving forward even in the face of a Covid pandemic," Biden said.
The President said that the new report shows "we're actually making real progress," shrugging off concerns in Washington about the jobs numbers not meeting their targets. 
"Right now, things in Washington, as you all know, are awfully noisy. Turn on the news and every conversation is a confrontation. Every disagreement is a crisis. But when you take a step back and look at what's happening, we're actually making real progress," Biden said. "Maybe it doesn't seem fast enough. I'd like to see it faster and we're going to make it faster. Maybe it doesn't appear dramatic enough. ... We're making consistent and steady progress, though." 
The President also used the speech to make the case for his infrastructure and social safety net legislative agenda.
"We need to stay focused on what these bills mean for the people, who are just looking for a little bit of breathing room, a fair chance to build a decent middle-class life, to succeed and thrive instead of just hanging on by their fingernails," Biden remarked. "We need to keep an eye -- an eye -- on what's fundamentally at stake for our country: the ability to compete and win the race of the 21st century as we did in the 20th century."
Labor Secretary Marty Walsh told "CNN Newsroom" on Friday that there were some "bright spots" in the report, including the women's participation unemployment rate down to 4.2% and unemployment among Black women is down to 7.3%.
"This is not all doom and gloom here today. Certainly, we know, I would love to be on this show saying we added 3 million jobs to the economy and now we can go on to something else, but unfortunately we're still -- we're not there yet," he conceded.
As for what this portends for Democratic negotiations on the Biden economic agenda, Walsh made the argument that the weak job growth bolsters the need to pass the President's legislative priorities.
"I would hope that, you know, members of Congress and members of the Senate today look at this jobs report and see where the shortfalls are and understand that these investments that the President wants to make in these areas will have long-term, lasting, positive impacts on our economy moving forward," he continued. 
The White House released a report on Thursday highlighting support for vaccine requirements across business and labor communities. 
The report also details the positive economic effects among communities with high vaccination rates, including that "small business employee hours grew faster and stayed higher during the rise of the Delta variant in the states that have higher working-age vaccination rates, versus states with lower vaccination rates."
CNN's Anneken Tappe contributed to this report. 
 (CNN)When CNN Chief Medical Correspondent Dr. Sanjay Gupta sat down for a three-hour conversation on "The Joe Rogan Experience" podcast, the chief topic was Covid-19. 
Gupta and Rogan -- whose views often were at odds -- discussed the pandemic, vaccines, potential therapeutics and the risk coronavirus poses to children and young people, among many other subjects. 
Here are four key moments from the conversation between Gupta, author of the new book "World War C: Lessons from the Covid-19 Pandemic and How to Prepare for the Next One," and Rogan, one of the world's most influential podcast hosts.
Rogan agrees a lot of 'vulnerable people' should get vaccinated
Rogan, who is not vaccinated against Covid-19, has previously expressed skepticism that young, healthy people should get the shot. But in his conversation with Gupta, Rogan agreed that certain people who are vulnerable to the virus should get inoculated against Covid-19, particularly those who are obese or elderly. 
"That's half the country, probably more, when you talk about obesity and diabetes and the other comorbidities that are associated with this," Gupta said. "You're talking about hundreds of millions of people. ... Doesn't that make the case that we need to vaccinate?" 
"I think it makes a good case to vaccinate vulnerable people, and that includes obese people," Rogan said. 
Rogan announced last month he had tested positive for Covid-19, but when asked if he wished he were vaccinated before he tested positive, Rogan said no, adding he got over the virus "pretty quickly." 
"My thought was, I'm a healthy person, I exercise constantly, I'm always taking vitamins. I take care of myself. I felt like I was going to be OK. And that was true, it was correct. I'm happy I got through it. I don't wish it upon anyone. It wasn't fun, but it wasn't the worst cold I've ever had, and I got over it fairly quickly, relatively speaking." 
But, Rogan added, "I'm not recommending anybody get infected."
"So, they should get vaccinated," Gupta said. 
"I think a lot of people should get vaccinated," Rogan said.
Gupta explains why Covid-19 is still a serious disease for children
The pair also discussed the risk posed to children by either Covid-19 or the vacci"""
    wordcloud(cnn_text)
    fox_text = """'Gutfeld!' panel reacts to the media coverage of the influential podcasted after his COVID-19 diagnosis
CNN chief medical correspondent Dr. Sanjay Gupta made headlines Thursday for appearing on Joe Rogan's podcast despite the liberal network's lengthy history of attacking the influential media personality. 
Gupta sat down for a lengthy conversation where he was grilled on why children should be forced to take the COVID vaccine since they face minimal risk from the virus. Rogan also pressed his guest on why CNN characterized the ivermectin he took to recover from COVID as a "horse dewormer." 
CNN’s top doctor was cordial to Rogan during the sometimes-combative interview, but the reception Rogan had previously received from CNN was far more hostile. 
Earlier this month, CNN's weekend anchor Jim Acosta went on a rant condemning the "garbage," "COVID disinformation" Rogan says on his podcast after he baselessly speculated that President Joe Biden received a fake booster shot for the cameras. 
JOE ROGAN FORCES DR. SANJAY GUPTA TO ADMIT CNN SHOULDN'T HAVE CALLED HIS COVID TREATMENT ‘HORSE DEWORMER’
"It is so pernicious," Acosta reacted. "We can write off and say, ‘Oh, this is just some guy with a podcast’ and ‘What’s the big deal?' and ‘he’s a comedian.' It's dangerous. It's just so dangerous."
"I wish he would just knock it off. It's not worth it, it's not worth the numbers, the data, the whatever the metrics that they get, podcasters. It's just not worth it. Please stop," Acosta pleaded to Rogan. 
CNN extensively covered Rogan's announcement that he had tested positive for COVID, repeatedly hammering him for his past rhetoric on the vaccine. 
"No one is happy for gloating over the fact, at least not here, that Joe Rogan tested positive for COVID, OK? … But Joe Rogan has been dismissive of vaccines," CNN anchor Don Lemon said. "You have a responsibility. You have a responsibility when you have a platform as big as Joe Rogan's."
After Rogan announced in September that he tested positive for COVID, CNN's left-wing media guru Brian Stelter slammed Rogan for using various treatments amid his recovery including ivermectin, which Stelter referred to as a "horse deworming medication," that would encourage others to try them as well. 
"That's the upside-down world we're in with figures like Joe Rogan," Stelter told Anderson Cooper.
Stelter later lectured Rogan during his appearance on Lemon's show, insisting "it's not enough" for him to say he's "not anti-vax" but that he must be "pro-vax."
"You gotta come out when you have a big platform and share your experience getting vaccinated, helping your neighbors. And Joe Rogan has done the opposite," Stelter said. "Yes, he will probably be fine, he will probably get better, but he has sent all the wrong signals to date with this kind of contrarianism where, you know, if the government says one thing, he has to do the opposite. That is the rotten core of conservative media right now."
JOE ROGAN BLASTS MEDIA LIES ABOUT HIS COVID TREATMENT: ‘DO I HAVE TO SUE CNN?’
"OutFront" host Erin Burnett also knocked the "controversial" podcast host for using a "livestock drug."
"New Day" co-hosts accused Rogan of "giving air to anti-vaccine narratives" in April after Rogan opined that young, healthy people shouldn't have to get the COVID vaccine, which he later walked back. 
CNN anchor Jim Sciutto suggested that Rogan was "endangering" the health of his listeners and invited Dr. Anthony Fauci to push back against the podcast host. Analyst John Avlon said Rogan was "playing footsie" with anti-vaccine impulses.
It's not just Rogan's rhetoric towards COVID that upsets CNN. Lemon lashed out at the podcast star for predicting "straight White men" will be silenced amid a growing "woke" culture. 
"Acknowledging the oppression, discrimination or differences of others does not silence anyone else," Lemon pushed back. "No matter what he has said, he has not been silenced! He has a huge megaphone with millions of loyal listeners, all of whom every single day say whatever they want… No one is stopping Joe Rogan or any other ‘straight White men’ from expressing themselves. Period."   
Despite the network's hosts and pundits often criticizing Rogan, it appears CNN granted Gupta its blessing to sit down with Rogan. CNN even published a lengthy essay Gupta wrote defending his appearance on the podcast. CNN has since embraced the interview on air, too, while largely downplaying or ignoring the exchange about ivermectin in which Gupta said CNN shouldn’t have mocked the drug as a "horse dewormer."  
Fox News’ Brian Flood contributed to this report. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News correspondent Rich Edson has the latest on where each gubernatorial candidate stands on the campaign trail.
New Jersey Gov. Phil Murphy is seeking reelection next week, attempting to become the first Democrat to be reelected governor in the Garden State since 1977.
Murphy, who graduated with a degree in economics from Harvard University in 1979 and worked for Goldman Sachs for 23 years, got his start in politics when he served as the National Finance Chair of the Democratic National Committee between 2006 and 2009, serving at the time under DNC Chair Howard Dean. 
After former President Barack Obama was elected in 2008, Murphy was appointed as U.S. ambassador to Germany and served in the role until 2013.

      New Jersey Governor Phil Murphy
      (USA TODAY NETWORK via Reuters Connect)
Speculation started shortly after his time as ambassador to Germany that Murphy might launch a bid to become New Jersey's governor in 2013, but he ultimately decided against it.
NJ GOV. MURPHY'S MULTIPLE CONTROVERSIES THREATEN CHANCES TO BE FIRST DEM REELECTED IN OVER 40 YEARS
A vocal critic of former New Jersey Gov. Chris Christie, Murphy announced his bid for the Democratic nomination for governor in 2016, officially entering the 2017 New Jersey gubernatorial election. 
Earning the endorsements of both of New Jersey's Democratic U.S. Senators, Bob Menendez and Corey Booker, Murphy easily won the Democratic primary with 48.1% of the vote. Facing off against Republican nominee Kim Guadagno, Murphy won the general election by a margin of 55.7% to 42.2%.
Murphy has pushed several progressive policy proposals in his time as governor, including the legalization of recreational marijuana, a $15 per hour minimum wage and guaranteed paid sick leave for employees.
Now running against Republican candidate Jack Ciattarelli in next Tuesday's election, Murphy's campaign has focused on his response to COVID-19 and creating more jobs for the state. He has also called for criminal justice reform, arguing that minorities are at a systemic disadvantage under the current criminal justice system.

      Phil Murphy, New Jersey's governor. (Mark Kauzlarich/Bloomberg via Getty Images)
      
But the governor faces several challenges in his bid for reelection, most notably when it comes to his heavy-handed approach to dealing with the COVID-19 pandemic.
One controversial policy was his decision to order nursing homes to readmit residents recovering from COVID-19, drawing comparisons to former New York Gov. Andrew Cuomo and criticism that the order caused unnecessary deaths.
Republicans in the state slammed the governor following the release of footage from a campaign official saying he will require residents to be vaccinated against COVID-19 if he were to be reelected.
Murphy has also faced criticism for failing to address the state's nation-high property taxes, an issue he famously dismissed in 2019, reasoning if "you’re a one-issue voter and tax rate is your issue, we’re probably not your state." 

      FILE - New Jersey Gov. Phil Murphy (Anne-Marie Caruso/The Record via AP, Pool)
      
But those comments came at a time of a mass exodus of residents from the state, with one analysis showing New Jersey had the highest rate of outbound migration in 2019.
Despite the challenges, current polling shows Murphy with a comfortable lead over his Republican challenger. According to the most recent polls collected by RealClearPolitics, Murphy's smallest advantage is six points in an Emerson poll conducted between Oct. 15-18. Other polling shows Murphy with an even larger advantage, including a new Monmouth poll that showed him enjoying an 11-point lead over Ciattarelli.
Michael Lee is a writer at Fox News. Follow him on Twitter @UAMichaelLee
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Congressional correspondent Aishah Hasnie discusses the backlash Merrick Garland is facing from Senate Republicans on ‘Special Report’.
Republican members of the House Judiciary Committee on Wednesday requested the assistance of the National School Boards Association (NSBA) for their probe into what they called "troubling attempts" by the White House and the Justice Department to target parents.
"We are investigating the troubling attempts by the Department of Justice and the White House to use the heavy hand of federal law enforcement to target concerned parents at local school board meetings and chill their protected First Amendment activity," began the letter, which was signed by 19 members of Congress and addressed to NSBA president Viola Garcia and other officers of the organization's board of directors.

      Rep. Greg Steube, R-Fla., holds photos from the Jan. 6, attack on the Capitol as he questions Attorney General Merrick Garland during a House Judiciary Committee oversight hearing of the Department of Justice on Thursday, Oct. 21, 2021, on Capitol Hill in Washington. (Greg Nash/Pool via AP)
      
The House Judiciary members mentioned the Sept. 29 letter that the NSBA sent asking the Biden administration to review threats and violence against education administrators and schools to determine if they violate the Patriot Act and hate crime laws. The letter said that some "acts of malice, violence, and threats against public school officials" could amount to domestic terrorism.
The request came amid clashes between angry parents and educators over COVID-19 policies and critical race theory being taught in classrooms.
Days later, on Oct. 4, Attorney General Merrick Garland sent a memo directing the Federal Bureau of Investigation (FBI) and U.S. Attorneys’ Offices to address the "disturbing spike in harassment, intimidation, and threats of violence."

      FILE PHOTO: FILE PHOTO: Angry parents and community members protest after a Loudoun County School Board meeting was halted by the school board because the crowd refused to quiet down, in Ashburn, Virginia, June 22, 2021.
      (REUTERS/Evelyn Hockstein/File Photo)
The GOP members also pointed out the evidence that the NBSA was communicating with the Biden administration before the Sept. 29 letter, noting how less than a month later, the Biden administration announced that Garcia had been appointed by Secretary of Education Miguel Cardona to the National Assessment Governing Board (NAGB), which has oversight over the National Assessment of Educational Progress (NAEP).
BIDEN ADMIN GIVES POST TO NATIONAL SCHOOL BOARDS ASSOCIATION CHIEF WHO SIGNED ‘DOMESTIC TERRORISM’ LETTER
After stoking outrage, the NSBA walked back its rhetoric, saying in an Oct. 22 memo that leaders "regret and apologize for the letter" and that "there was no justification for some of the language" used. Garland has also distanced himself from the letter's language, though Republican members of the Senate Judiciary Committee excoriated him for it when he testified Wednesday.

      Attorney General Merrick Garland is sworn in during a Senate Judiciary Committee hearing examining the Department of Justice on Capitol Hill in Washington, Wednesday, Oct. 27, 2021.
      (Tom Brenner/Pool via AP)
GARLAND REFUSES TO BACK AWAY FROM DOJ MEMO AFTER SCHOOL BOARD APOLOGY
The members of Congress went on to ask the NSBA to offer documents and communications that took place between the organization and the Biden administration in the lead-up to the Sept. 29 letter.
The NSBA was also asked to answer whether it will urge Garland to withdraw or rescind his Oct. 4 memo.
The organization was given a deadline of Nov. 10 to provide the requested information.
The NSBA did not respond to Fox News' request for comment in time for publication.
Fox News' Jessica Chasmar contributed to this report.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top entertainment and celebrity headlines are here. Check out what clicked this week in entertainment.
Bryan W. Carpenter believes the tragic death of Halyna Hutchins reveals an ongoing problem in Hollywood.
Authorities are investigating after confirming that a prop firearm discharged by Alec Baldwin while producing and starring in the Western film "Rust" killed the cinematographer and wounded the director.
Santa Fe County Sheriff’s officials said Hutchins, 42, and Joel Souza were shot on the rustic film set in the desert on the southern outskirts of Santa Fe. Hutchins was airlifted to the University of New Mexico Hospital, where she was pronounced dead by medical personnel, the sheriff’s department said. Souza, 48, was taken by ambulance to Christus St. Vincent Regional Medical Center where he has since been released. Production has been halted.
"We all know that movie sets are very hectic, so following safety protocol becomes even more paramount at that point," the weapons armorer told Fox News. "There’s no reason a live round should ever be within any distance of a movie set."
ALEC BALDWIN'S 'RUST' SHOOTING BEING INDEPENDENTLY INVESTIGATED BY GLORIA ALLRED: 'MANY UNANSWERED QUESTIONS'

      Halyna Hutchins is survived by her husband and their son.
      (Photo by Mat Hayward/Getty Images for AMC Networks)
Carpenter is the founder and president of New Orleans-based Dark Thirty Film Services, LLC, which has been involved with several high-profile projects over the years, including "The Expendables," "Bad Country," "NCIS: New Orleans," "Queen of the South," and "22 Jump Street" among others.
"The primary role of an armorer on the set is to maintain the safety of the firearms being used," he explained. "That's the most important thing. The secondary responsibilities are to work with the talent and make sure they look correct while using the firearm while filming. We also work with the director to make sure the shots line up properly and safe distances occur."
"I have worked on some lower budget shows, but I pick and choose the ones I work on and I know the crews are good and safe," he shared. "You need to work with good quality studios, production offices and prop masters who follow safety protocol properly."
Once a weapons armorer reviews the script, Carpenter said the appropriate firearms that complement the time period or character are ordered from reputable "prop houses" in the United States. Whenever they’re being used, multiple safety checks are required.

      The Bonanza Creek Film Ranch in Santa Fe, New Mexico, is shown Friday, Oct. 22, 2021. Actor Alec Baldwin fired a prop gun on the set of a Western being filmed at the ranch on Thursday, Oct. 21, killing the cinematographer, officials said. The director of the movie was wounded, and authorities were investigating.
      (AP Photo/Andres Leighton)
"You check them to make sure they’re all clear," he said. "You’re checking for blank rounds. There should never be a thought that there’s a live round in there. When you’re checking for blank rounds, you’re always looking for the possibility of anything else being there. You lock the weapons in the safe when they’re not in use and they must stay there. Those guns cannot be used for anything else. I always prep what I’m going to be using the next day in the safe. I separate everything and keep it locked. And above all, every time you open the safe, you check them."
"You can never have too many checks," he said. "If you think you’ve checked too much, check again. No one touches those weapons or uses them for anything else. The weapons only come out of the safe when it’s time to use them for a scene. And right before it’s handed to the talent, there’s a verification process. You make sure there are no obstructions in the barrel and that the cylinders, the chambers are clear. At a minimum, there should be two people present to verify that the weapon is in the condition that you say it is."
Problems were already plaguing the "Rust" production before Baldwin, 63, fired the fatal shot. Hours before, a camera crew for the movie walked off the job to protest conditions and production issues that included safety concerns.

      There were safety concerns before Halyna Hutchins' tragic passing.
      (Photo by Sam Wasson/Getty Images)
Disputes began almost from the start in early October and culminated with seven crew members walking off several hours before Hutchins was killed. The crew members had expressed their discontent with matters that ranged from safety procedures to their housing accommodations, according to one of those who left.
At a rehearsal on the film set, the gun Baldwin used was one of three that an armorer had set on a cart outside the building, according to court records. An assistant director, Dave Halls, grabbed a prop gun and handed it to Baldwin, indicating incorrectly that the weapon didn’t carry live rounds by yelling "cold gun."
Carpenter said he’s been vocal over the years about the need for actors to attend safety training when handling weapons on set.
"It’s a dollars and cents thing," he said. "They don’t want to spend the time bringing the personnel in to do it. They don’t want to spend the time paying the actor to have to come out and go through a training class and then have to bring their staff with them. Maybe it’s not in their contract. And if you think they were cutting corners before COVID, just imagine how bad it is now when they’re trying to save money because of all the dollars they’re spending on all the COVID regulations they’re putting out."
ALEC BALDWIN ‘RUST’ SHOOTING COULD HAVE BEEN AVOIDED IF ‘IF THEY HAD DONE A PROPER SAFETY CHECK’: PROP MASTER

      On social media, Alec Baldwin said his ‘heart is broken’ and he's ‘fully cooperating with the police investigation.’
      (Jim Spellman/Getty Images)
Carpenter recalled how he was part of a "gun-heavy show" months ago when he asked the studio "multiple times" if he could take the actors out for safety training. Carpenter alleged he was told no because "we don’t have that kind of money."
"They just would not do it," he said. "So on my own time, I got with the actors individually… One told me, ‘I want to know how to do this safely.’ So they took their own time to take a safety training class. You have studios that do care and want to do it the right way. But others just want to get through it and move on. But I do think safety training should be mandatory."  
In addition, Carpenter said there needs to be a national certification for armorers. Some locations like New York and California, he said, certify armorers. However, "the rest of the country pretty much doesn’t have anything."
"If you’re down in the south and you’re hiring an armorer, anybody can convince a studio that they can do the job to potentially get it," he explained. "There needs to be a vetting process where a professional armorer can provide their certifications, the safety schools they attended, their past work and what became of it, and why they’re considered a safe person to handle the job."
STARS IN DISBELIEF OVER ALEC BALDWIN FATAL PROP GUN SHOOTING: 'MISMANAGED SET'

      Mourners attend a candlelight vigil for Halyna Hutchins at IATSE West Coast Office on October 24, 2021 in Burbank, California. 
      (Photo by Rodin Eckenroth/Getty Images)
Without a national certification, studios, especially with a minimal budget, may be swayed to "save a dollar" and hire someone who has a lesser rate but doesn’t fully meet the qualifications, he pointed out.
"That’s a recipe for disaster if you ask me," said Carpenter. "I had a show a few years back, a lower budget show. One of the line producers asked me if I would come in and work. I gave her my quote… She came back to me a few days later and said, ‘Some of the producers got a quote from another guy who is well under your quote.’ It’s a small circle. They called the guy’s name out and I had never heard of him. I called the union to check if they’ve ever heard of him and they haven’t either. With a little research, I found out he had worked as an extra on two movies in the state of Alabama. After working two shows as an extra, he’s now bidding on a job as a professional armorer who is, and I quote, ‘bringing his own guns.’"
Carpenter claimed he bowed out of the project and the person in question was hired.
"By the grace of God, no one got hurt," he said. "But that shows you how things are when people are willing to save money but don’t care if [the individual is] trained properly or even has any experience whatsoever. Three things on a movie set can kill you fast – stunts, effects and armorer. And generally, they will cut the budget on all three of those more than they will cut on anything else."
'RUST' MOVIE HEAD ELECTRICIAN SAYS HE WAS 'HOLDING' HALYNA HUTCHINS IN HIS 'ARMS WHILE SHE WAS DYING'

      Halyna Hutchins was a rising star in the cinematography world when she was hit with a projectile on set that ultimately killed her.
      (Photo by Fred Hayes/Getty Images for SAGindie)
New Mexico workplace safety investigators are examining if film industry standards for gun safety were followed during the production of "Rust." The Los Angeles Times, citing two crew members it did not name, reported that five days before the shooting, Baldwin’s stunt double accidentally fired two live rounds after being told the gun didn’t have any ammunition.
A crew member who was alarmed by the misfires told a unit production manager in a text message, "We’ve now had 3 accidental discharges. This is super unsafe," according to a copy of the message reviewed by the newspaper. The New York Times also reported that there were at least two earlier accidental gun discharges; it cited three former crew members.
One crew member said he never witnessed any formal orientation about weapons used on set, which normally would take place before filming begins. He also said only minimal COVID-19 precautions were taken even though crew and cast members often worked in small enclosed spaces on the ranch.
Hannah Gutierrez Reed, the film’s armorer, gave an interview in September to the "Voices of the West" podcast in which she said she had just finished her first movie in the role of head armorer, a project in Montana starring Nicolas Cage titled "The Old Way." As for Halls, he was fired from a separate project in 2019 after a crew member on "Freedom's Path" incurred an injury from a prop gun.
As the investigation continues, Carpenter hopes Hollywood will get its act together.
"This should have never happened," he said.
FDNY Firefighters Association President Andrew Ansbro shares the consequences of forcing a vaccination mandate.
New York City’s municipal workforce has been warned by Mayor Bill de Blasio to be vaccinated by Nov. 1 or face unpaid leave which FDNY Firefighter Association President Andrew Ansbro argues will only cause chaos.
In an appearance on Fox News Radio’s "Brian Kilmeade Show," the firefighter expressed how the department refuses to go down without a fight which will only lead to fewer workers on duty and more emergencies waiting to be responded to.
"The staffing just is not there, there’s no way to do it," he said. "The response times are going to go through the roof. We’re just not going to be able to get to the emergencies in time."
NYC WORKERS PROTEST VACCINE MANDATE: ‘WE WILL NOT COMPLY!’
"Fires are going to burn longer. Heart attack victims are going to be laying on the floor longer," he continued. "People in stuck elevators are going to be stuck there for hours if not days."

      Andrew Ansbro, FDNY Uniformed Firefighters Association President, speaks during a news conference to address a newly announced COVID-19 vaccine mandate, Wednesday, Oct. 20, 2021, in New York. (AP Photo/John Minchillo)
      
According to Ansbro, 45% of New York City firefighters are unvaccinated and the number who have shown up in the last week to receive the vaccination is most likely "pretty small." The firefighter predicted that come Nov. 1, the city will be forced to close down 30 to 40% of the firehouses.
"On Friday, when they’re tallying the numbers of who complied and who didn’t, they’re going to be faced with a stark reality that they’re going to have to close firehouses down," he said.
Ansbro revealed that firefighters are instead opting for early retirement and the number of people who normally retire in a month has been recorded in just two days. The department was told that medical and religious exemptions would be available but they would be "highly scrutinized" and very unlikely.
"The religious exemption is going to be held to the standard which is as per the needs of the department and the department needs you vaccinated, according to them," he said. "So they can basically waive any religious exemption and we expect them to do that."

      FDNY ambulances are seen entering and leaving the emergency room at Queens Hospital Center, Monday, April 20, 2020, in the Jamaica neighborhood of the Queens borough of New York. (AP Photo/Mary Altaffer)
      
Ansbro is pushing to counteract the "immoral" mandate by persuading the federal government to reinstate the test or vaccine option for the FDNY and other city agencies, coming to terms with the fact that living with COVID is the new norm.
"This is not a crisis," he said. "Months ago, the mayor had his parade to say this is over. As far as we’re concerned, it’s over… Members need to have a choice to either get tested or vaccinated."
"The mayor is going to be faced with either sending us home or sticking to his guns," he concluded. "And his guns are going to get New York City residents killed… When this city goes into utter chaos on Nov. 1, be ready to pick up the pieces that the mayor causes."
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Story #2: The most exciting of tragic days in college football.
Story #3: Will shares what he considers the good news and bad news in America’s education system.

Tell Will why he is right…or wrong.
Democrats are getting ready to make some cuts to their original $3.5-trillion spending package in order to get it passed both houses of Congress after moderate Senators Joe Manchin (D-WV) and Kyrsten Sinema (D-AZ) made it clear they would not support the multi-trillion dollar bill. Rep. Henry Cuellar (D-TX) joins today to weigh in on the infrastructure and budget reconciliation bill, what needs to be included and if the Biden administration is to blame for the ongoing inflation and labor shortages since he took office nine months ago.
Plus, commentary by FOX News contributor Joe Concha.
Former Facebook Product Manager Frances Haugen is now known as the Facebook Whistleblower, after her recent testimony in front of the Senate’s Consumer Protection Subcommittee. Haugen claimed that Facebook harms children, sows division, and undermines democracy in pursuit of breakneck growth and astronomical profits. FOX News Congressional Correspondent Aishah Hasnie covered the hearing and the aftermath.
The U.S. military fully withdrew from Afghanistan on August 30th, 2021. However not all U.S. citizens and Afghan allies were evacuated, leaving many vulnerable as they found themselves stranded in a nation now controlled by the Taliban. In response to this dangerous situation, many veterans have taken the initiative to organize the safe return of these people from Afghanistan to America. Afghan War veteran, former U.S. Navy Lieutenant Commander and Co-Founder of Project Dynamo, Bryan Stern joins to break down how he chartered a flight full of Americans and allies out of Kabul, how Project Dynamo’s donations made the safe return of hundreds of people possible and why his experience as a veteran and 9/11 first responder drove him to take action to make sure there was no one left behind.
Plus, commentary by syndicated columnist and author of “America’s Expiration Date,” Cal Thomas.
Plus, West responds to MSNBC’s Joy Reid saying he is “Right of Attila the Hun”
David Asher, a senior fellow at Hudson Institute and former investigator into covid-19 origins at the State Department joined the Guy Benson Show to discuss the recent reporting on the origins of Covid-19 in China and ‘gain of function’ research.  
Asher reacted to recent reporting on the NIH’s involvement in funding ‘gain of function’ research saying, 
“The key thing is gain of function research. I can categorically say from my perspective as investigator was being funded by the NIH at the Wuhan Institute from at least 2015, probably longer, I talked to maybe 50 U.S. government scientists, including NIH scientists, and they were in general agreement that the research that was done and reported in published papers, including a famous paper by a guy named Dr. Ralph Baric from University of North Carolina and Dr. Shi, the bat lady at one institute, did constitute gain of function research.”
Asher added, 
Over the summer, the National Collegiate Athletic Association adopted a temporary policy that would allow college athletes to begin to benefit and get paid for their name, image, and likeness. The NIL policy changes came on the heels of a unanimous Supreme Court decision that the NCAA cannot limit student-athletes with education-related benefits. Along with this court case, the issue was subject to major public scrutiny, with some college athletes speaking out against the rule as unfair and outdated. One of these college athletes, Rutgers University basketball star Geo Baker joins to explain why he found the NCAA rules on name, image, and likeness inequitable for student-athletes, how people met home with support and negativity when he chose to speak out against this policy and how this change in college sports is going to have a profound impact on the lives of the players as well as the fans.
Plus, commentary by Fox News contributor Liz Peek.
So, is it possible America has finally turned the corner on the pandemic?
Earlier this week, Former Assistant Secretary for Health under President Trump, Admiral Brett Giroir joined host Jessica Rosenthal to give his take on America’s ongoing effort to combat the coronavirus and the questions regarding boosters, vaccine mandates for children and the reliability of testing.
Dr. Giroir did see optimistic about the coming months, but still offered advice to families on how to protect themselves from future surges in the virus.
He also weighed in how our country reacted to COVID, what mistakes we made and whether or not we’re prepared for future pandemics.
The interview was too long and we could not include everything Dr. Brett Giroir had to say. On the FOX News Rundown Extra you will hear our entire conversation.
Dr. Marty Makary, Fox News Contributor, Surgeon, and A Professor Of Health Policy At The Johns Hopkins School Of Public Health joined the Guy Benson Show to talk about the John Hopkins led study on covid-19 natural immunity. 
Dr. Makary talked about the study saying, 
Vaccine mandates have become a central and polarizing issue for many Americans. With the COVID-19 vaccine now widely available, federal employees and the U.S. military have been required to get the coronavirus vaccine, however some states are bucking this trend. On Monday, October 11th, Governor Greg Abbott of Texas issued an executive order that would block any vaccine mandates within his state, even for private businesses. Dr. Jerome Adams, 20th U.S. Surgeon General and Director of Health Equity Initiatives at Purdue University joins to discuss the nuances of COVID-19 vaccine mandates, a recent controversy within the Southwest Airlines pilots union over the vaccine mandates, and his belief the government should not restrict how employers keep their employees healthy. Later, he shares his optimism on the return to normalcy and how soon he expects a COVID-19 vaccine for children.
Plus, commentary by former Rep. Jason Chaffetz, host of the Jason in the House podcast.
Dr. Nicole Saphier, Board Certified Medical Doctor, Senior Fox News Medical Contributor joined the Guy Benson Show to discuss the data behind the need to vaccinate children against covid-19. 
Dr. Saphier gave her thoughts on the need to vaccinate children against covid-19 saying,  
Later, Jason sits down with U.S. Senator Cynthia Lummis (R-WY) to discuss how she became the first female senator of Wyoming. Senator Lummis explains how being responsible for livestock growing up has shaped the way she feels about the role of family, individuals, and government.

A new wave of COVID-19 vaccine guidance was released this week. Moderna and Johnson & Johnson joined Pfizer as an FDA panel approved booster shots for American adults over 65, living in long-term care, or with underlying conditions. Meanwhile, the Biden Administration rolled out its plan to begin vaccinating 28 million elementary-aged kids as early as November, should the FDA sign off. Senior Scholar at Johns Hopkins Center for Health Security, Dr. Amesh Adalja makes sense of these new recommendations.
Nurses have played a vital role throughout the coronavirus pandemic, working tirelessly on the front lines to save lives, but they’ve been doing it even before COVID-19. Best-selling author James Patterson and combat veteran Matt Eversmann join today’s FOX News Rundown to talk about their new book and the FOX Nation special “E.R. Nurses” that honors the jobs of nurses and features first-hand accounts of the highs and lows of being in the Emergency Room.
 Plus, commentary by Jimmy Failla, host of “Fox Across America with Jimmy Failla.”
A new book has been released from the only national security advisor to witness all four years of the Trump administration, from the 2016 campaign trail to the end of President Trump’s term in office. Former National Security Advisor to both President Trump and Vice President Pence, retired Lieutenant General Keith Kellogg joins to discuss his book, ‘War By Other Means: A General in the Trump White House.’ He walks us through his four years with the Trump administration and how he saw a different side of the former President than the one portrayed in the media and the way he encouraged a diversity of opinions within his circle. Gen. Kellogg also discusses how he saw events unfold during the January 6th Capitol riot, why U.S. involvement in Afghanistan had disastrous results and the issue of China acquiring hypersonic weapons before the U.S.
Plus, commentary by FOX Nation host Tammy Bruce.
“Hunter Biden, in all honesty, is a national security threat. I can only imagine if Don Jr., Eric Trump or Ivanka were selling artwork, what the media would be doing now, what the Democrats in Congress would be doing. But here you have a situation where Hunter Biden clearly sold access to the Biden family in the past, to Ukraine, to Libya, to China. And now we know that Hunter Biden’s under federal investigation in Delaware, in New York and in Washington, D.C. for tax evasion, among other things. So here’s a guy that has a pattern of bad behavior. And Joe Biden’s first nine months have been marked by questionable decisions like why aren’t you wanting to find out the origination of COVID 19? Why are we letting China off the hook? Why did we rejoin the World Health Organization without holding China accountable? Why did we just leave the weapons and the military base behind for the Taliban? There’s so many things that Joe Biden has done that make no sense. And you look at Hunter and you wonder, is there a pattern here, is is Joe Biden compromised? I don’t know if he is or not, but they’re not doing anything to relieve my concerns.”
This week we heard from President Biden’s top military officials, Defense Secretary Lloyd Austin, Chairman of the Joint Chiefs of Staff General Mark Milley and CENTCOM Commander General Kenneth McKenzie during a Senate Armed Services Committee hearing on the U.S. troop withdrawal from Afghanistan. Rachel speaks with General Jack Keane, FOX News Senior Strategic Analyst, and retired four-star general, about the key takeaways from this week’s hearing and the future of America’s war against terrorism.
“You never know what underlying health factors some players may or may not have. But ultimately, you’re not getting vaccinated for yourself, you’re getting vaccinated to protect the people around you as well. So it’s another one of those selfless acts that has to be thought about when you’re playing on a team in the league and you always surrender yourself for bigger team or group.”
“There’s choices and consequences. You can make any choice you want, and you just got to deal with whatever the consequences come your way. So I decide whether I want or not to get a vaccine. If I want to play, these are the rules that I have to play by. It’s a big sandbox, and if there are rules, there are things that you have to follow. And if that’s what’s mandated by the league and I want to be a part of the league, that’s what I got to do. Now if I choose not to do that, that’s fine too. It’s your choice.”
Many industries have been changed by the COVID-19 pandemic, the real-estate market is no different. We saw in the beginning of the pandemic there was a housing boom as many people left big cities for homes in more suburban areas. Many home owners elected to renovate their houses and one of the more popular additions was a home office to accommodate Americans working remotely as a result of the coronavirus. Realtor and host of HGTV’s “Love It or List It” David Visentin joins to talk about the show and some of the major shifts he saw during the pandemic regarding selling or renovating homes, and what pandemic-related changes he believe are here to stay.
Don’t miss the good news with Tonya J. Powers.
Plus, commentary by Fox News contributor and author of the new book, “Rigged”, Mollie Hemingway.
President Biden announced a new 1.75 trillion-dollar social spending framework, calling it a  “historic economic framework” that his administration believes can pass a party line vote in Congress. As the President soon departed for his European trip to the G20 and climate change summits, the framework currently in place did not have all the details of the domestic spending package finalized. FOX News Sunday anchor, Chris Wallace joins to discuss whether this package will ultimately pass, why the President is pushing for broad sweeping legislation without a sizeable majority in Congress, whether this package would have substantial impact on fighting climate change and how the results of the Virginia governor’s race could change how Democrats run their campaigns in 2022.
Don’t miss the good news with Tonya J. Powers.
Plus, commentary by FOX Nation host Tom Shillue.
“I think there’s a distinction between the politics of his era and today, and I think generals are not immune to that. I have a decent relationship with General James Mattis and I respect him, I think he’s a good leader, a great leader. I think he believes what he says and says what he believes. But I think no one’s immune to politics these days. And so even General James Mattis, who had a very special respect from the troops, in the era of Trump, it becomes split. And I think Colin Powell suffered from quite a bit of that because, I think unlike many generals who tried to show themselves to be nonpolitical, I think he was more bipartisan. It’s not the ideal ideology of it, but the fact that it’s an American effort, and I want to support it. And so it’s certainly a sad day, it’s a sad day because we just don’t get to celebrate these men and women enough that do so much for us in the military. And he really did design, he and Schwarzkopf, really were the most effective leaders we’ve had in the last 40 years, if you go back from Vietnam forward.”
“I don’t know what these people’s political views are. I can tell you that every pilot that’s at home at Southwest isn’t a card carrying MAGA member. These are Americans who have their own personal morals and principles and values that they feel are being challenged to the umpteenth degree. And I bet some of these people are even vaccinated and just believe so, so sternly that they shouldn’t be mandated to that they’re not revealing that, and you know what? I don’t blame them. Companies have to understand you absolutely have the right as a private company to set your terms, but so do your employees walking out. But when it comes to a public service like police and fire, were do you have the bandwidth to kick these people out of your force?”
Fox News medical contributor Dr. Janette Nesheiwat discusses booster shots, Moderna and Johnson & Johnson alternatives, and new CDC, FDA guidance
Nearly 2 million COVID-19 vaccine booster shots were administered over the last week, White House COVID-19 Response Coordinator Jeff Zients announced at a briefing Friday. U.S. health authorities last week recommended a third dose of the Pfizer-BioNTech vaccine among certain high-risk groups to enhance protection against severe disease.
"As we vaccinate the unvaccinated, we’re also enhancing protection for vaccinated Americans through booster shots. We estimate that by day’s end, almost 2 million Americans will have rolled up their sleeves and gotten a booster shot. Nearly 2 million booster shots in the first week," Zients said during a virtual White House briefing Friday, calling it a "very strong start."

      Sept. 14, 2021: A syringe is prepared with the Pfizer COVID-19 vaccine at a clinic at the Reading Area Community College in Reading, Pa. 
      ((AP Photo/Matt Rourke) )
Earlier in the week, the Biden administration said more than 400,000 Americans received COVID-19 booster shots over the weekend just at pharmacies alone, and another million had signed up to get the extra jab after it was approved for seniors and high-risk people last week. Some 20 million Americans are now eligible for a COVID-19 booster shot, and in the months ahead, 60 million will become eligible as six months lapse from the primary series.
Dr. Imran Sharief, a pulmonary disease specialist in California, told Fox News of "busy, long lines" in the Northridge Hospital Medical Center booster clinic in Los Angeles, and in the Orange County community, Sharief said most seniors are receiving the booster and patients with immunocompromising conditions are receiving a third mRNA shot. According to  U.S. Surgeon General Dr. Vivek Murthy, three high-risk groups are eligible for the Pfizer-BioNTech booster about six months following the primary series:
TIME TO GET FLU SHOT IS NOW, DOCTORS URGE: OR ‘ROLL THE DICE’
A small fraction of Americans with moderate-to-severe immunocompromise were previously made eligible for a third dose as well. Murthy advised visiting vaccines.gov for thousands of locations nationwide offering COVID-19 booster doses.
The number of daily COVID-19 infections and hospitalizations in the U.S. are declining; as Sept. 27, the country was logging a seven-day moving average of 110,232 new daily cases, down 30.9% from 159,515 on Aug. 27, whereas new COVID-related hospitalization dropped 31% from 12,330 to 8,507 over the same time period.
GET THE FOX NEWS APP
"I think we're watching this [decline] very carefully and we really understand that the impact of Delta might be a little bit different," Dr. Rochelle Walensky, director of the Centers for Disease Control and Prevention (CDC) said during the briefing, adding in part, "as these cases come down, the most important thing that we can do is to continue to practice the mitigation strategies that we know work ... masking handwashing, distancing ventilation, but critically important, it's vaccination."
Fox News’ Breck Dumas contributed to this report.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Pfizer/BioNTech COVID-19 vaccine is 93% effective against COVID-19 hospitalization in youth, according to a U.S. Centers for Disease Control and Prevention study. 
The CDC said that among hospitalized patients in the U.S. ages 12 to 18 years, the effectiveness of two doses of Pfizer/BioNTech vaccine against COVID-19 hospitalization from June through September of this year was 93%.
The findings of the study, the agency said, could help to reinforce the importance of vaccination to protect U.S. youths against the virus.
FDA MAY APPROVE MIXING AND MATCHING COVID-19 BOOSTER SHOTS
In order to reach these conclusions, the CDC looked at this effectiveness in a test-negative, case-control study at 19 pediatric hospitals in 16 states, including 179 hospitalized case-patients and 285 controls. 
Forty-three percent of the case-patients were admitted into an intensive care unit, 16% received life support during hospitalization and 2% of those critically ill patients died. 
The agency noted that all 29 critically ill case patients and both deaths occurred among unvaccinated case patients.
Seventy-two percent of those analyzed had at least one underlying condition, including obesity, and 68% attended in-person school. 

      Pfizer COVID-19 vaccine doses are prepared for members of the community 12 years and up, Wednesday, May 19, 2021, at a clinic held by Community of Hope, outside the Washington School for Girls in southeast Washington. 
      (AP Photo/Jacquelyn Martin)
The case patients were hospitalized with symptomatic COVID-19-like illness and a positive SARS-CoV-2 reverse transcription–polymerase chain reaction or antigen test result.
Information regarding baseline demographic characteristics, clinical information about the current illness and SARS-CoV-2 testing history were obtained through parent or guardian interviews as well as the review of electronic medical records. 
Patients were considered to have received COVID-19 vaccination based on source documentation or by plausible self-report, though neither the Moderna vaccine nor the Johnson & Johnson vaccine were authorized for people less than 18 years of age at the time of the evaluation.
The study notably included persons categorized as unvaccinated or fully vaccinated and patients with partial vaccinated were discluded from the analysis.
FDA PANEL ENDORSES JOHNSON & JOHNSON COVID-19 VACCINE BOOSTER WITH 2-MONTH GAP FOR AGES 18 AND UP
The researchers used "descriptive statistics" to compare the characteristics of case patients and controls, including Pearson chi-square tests or Wilcoxon rank-sum test and vaccine effectiveness against COVID-19 hospitalization, which was calculated by comparing the odds of full COVID-19 vaccination among case patients and controls, determined from logistic regression models. 
Models were adjusted for the U.S. Census region, the calendar month of hospital admission, age, sex and race/ethnicity. While underlying health conditions and social vulnerability index were also assessed, they were not included in the final model because they did not change the odds ratio of vaccination by more than 5%.
Sensitivity analyses were performed and vaccine effectiveness was also stratified by age groups in addition to statistical analysis that was reviewed by the agency and other participating institutions.
Case patients more frequently resided in areas with higher social vulnerability, and vaccination coverage was 3% among case patients and 33% among controls. 
Diabetes was more prevalent among case patients, while neurologic or neuromuscular disorders were more prevalent among controls.
While the findings were reportedly consistent with efficacy data from the Pfizer/BioNTech clinical trial among persons ages 12–15 years, the CDC wrote that that trial had not been powered to assess efficacy against hospitalized COVID-19.
The CDC pointed out that, as of Monday, 46% of U.S. children and adolescents 12–15 years old and 54% of those 16–17 years old were fully vaccinated against COVID-19. 
"These data suggest that increasing vaccination coverage among this group could reduce the incidence of severe COVID-19 in the United States. Further, as in-person school attendance increases, multicomponent preventive measures to reduce the incidence of severe COVID-19 among adolescents, including vaccination, are imperative," the researchers concluded.
The White House announced Wednesday that children 5 to 11 years old would be able to get a Pfizer/BioNTech COVID-19 shot in a matter of weeks.
The Associated Press contributed to this report
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
"Is he a COVID baby?"  The waitress asked my husband and I this question about our sixteen-month-old son, as he gleefully gobbled up a plate of French fries.  We weren’t quite sure what she meant.
We laughed and smiled and she moved on. At least, I think we laughed and smiled.  At that moment, my mind was a mess. With that question, this innocent waitress had unwittingly opened a Pandora’s box of emotion --  trauma, fear, heartache and, ultimately, strength -- that I’d only just managed to close a short time ago, as things got back (we thought) to normal.
The new specter of the Delta variant had brought this all bubbling back up and this poor waitress wrenched it to the surface. 

      Vanessa Santos pictured on vacation with her son in Michigan,
      (Vanessa Santos)
Yes, my son is a COVID baby. He was born in the spring of 2020, during the peak pandemic pandemonium. And I’m a COVID mom. There are thousands of us, maybe millions.  We’ve been through the wringer, and we’re ready for whatever comes next.
DR. MARC SIEGEL: COVID PREVENTION, TREATMENT AND CURES – SURPRISING NEWS ABOUT WHERE WE ARE NOW
In my case, that means another baby. Our second little boy is due in December.  As I settle into my second COVID pregnancy -- a strange, surreal experience that I’m sure will only seem more surreal in years to come -- I’ve realized that I’ve gained a deeper appreciation for the awesome power of motherhood than I ever thought possible.

      The Santos family pregnancy announcement from spring 2021
      
My baby shower was scheduled for March 21, 2020, two days after Gov. Larry Hogan shut down the state of Maryland, where we live. That threw a wrench into our plans, but that was understandable. The world was changing. 
Then our doctor informed us that, due to COVID restrictions, only the patient would be allowed to enter their office for appointments -- nobody else.  I was making more doctor visits than usual, because early in my pregnancy they had detected a hormonal issue that required weekly sonograms to check on our baby.  I was already scared that at each successive visit I would get some life-altering news, and now I was being told I couldn’t have my husband beside me if that happened. 
DELTA COVID-19 VARIANT MORE DANGEROUS FOR UNVACCINATED PREGNANT WOMEN: STUDY
The news was full of stories of women in different cities having to give birth alone, or being quarantined separately from their own babies. Our own hospital cancelled their birthing classes. 
Our baby was due in May, and for several weeks I lived with the terrifying idea of having to go through the medical aspects of my first pregnancy and childbirth on my own.
 As I settle into my second COVID pregnancy, I’ve realized that I’ve gained a deeper appreciation for the awesome power of motherhood than I ever thought possible.
My husband is a scientist at the National Institutes of Health and was assigned to the Operation Warp Speed Task Force. His calming presence, knowledge, and guidance kept me sane. But whether your partner is a scientist or a welder or an insurance agent, you want them by your side as you bring your child into this world.
But an executive order was issued applying to both public and private hospitals to allow at least one person in the delivery room with the woman giving birth. My husband was there when I gave birth to our beautiful healthy baby son on May 1, 2020. 
COVID-19 VACCINATION AMONG PREGNANT WOMEN REMAINS LOW DESPITE SEVERE RISK
We couldn’t have any visitors in the hospital, and we came home to a strange hermetic world, with friends offering to drive by our house and wave through the windows. I politely declined -- it just seemed too weird. After a few weeks of being home alone, we started allowing visitors if they quarantined for the recommended period of two weeks -- but there was still tension in the air.  Could we trust them on their word alone?
The strange summer and dark winter of 2021 brought changes to everyone’s lives, and we were no exception. 
I left my beloved job for a fully remote position, because I wasn’t comfortable risking bringing something home to my infant son’s brand new immune system.  I know I am blessed to have had the ability to make that choice.
All of us who’ve had "COVID babies" have had to make different sacrifices.  It’s not just parents of the littlest ones, either - think of all the people who had to step in as teachers when "remote learning" fell apart, missed ball games or dance recitals, or didn’t get to see their child walk across the stage at graduation.  And many families faced the ultimate loss of a loved one who died from the disease.
We don’t fully know yet what the Delta variant will bring, but it does seem like we will be living with this thing, in some form or another, for a long time.  Through it all, people will keep making babies. 
That means more COVID babies, and more COVID moms. 
As someone who’s about to become a COVID mom for the second time, I couldn’t be more proud to be in the company of so many strong, courageous women around the world. 
We will not let this disease stamp out that most precious of human endeavors -- the continuation of life.
Vanessa Santos is the director of strategy and publication relations at the District Media Group. Vanessa lives in Bethesda, Maryland with her family and rescue dogs.
Get the recap of top opinion commentary and original content throughout the week.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Protests erupted in Italy as one of the most stringent anti-coronavirus measures in Europe went into effect Friday, requiring all workers, from magistrates to maids, to show a health pass to get into their place of employment. 
Police were out in force, schools planned to end classes early and embassies issued warnings of possible violence amid concerns that the anti-vaccination demonstrations could turn violent, as they did in Rome last weekend. 
The so-called "Green Pass" shows proof of vaccination, a recent negative test or of having recovered from COVID-19 in the past six months. Italy already required them to access all sorts of indoor environments, including restaurants, museums, theaters, and long-distance trains. 

      People gather and stage a No Green Pass protest in Turin, Italy on Friday. 
      (Marco Alpozzi/LaPresse via AP)
ROME’S MAYOR VOTED OUT OF OFFICE AMID CONTROVERSIES OVER CITY DECAY, TRASH, WILD BOARS 
But the addition of the workplace requirement has sparked heated debate and opposition in a country that was a coronavirus epicenter early in the pandemic and where vaccination rates are among the highest in Europe. 
"Today they are stepping on our Constitution," said an anti-vaccine protester, Loris Mazzarato. "I say NO to this discrimination." 
He was among the hundreds of demonstrators in Trieste, where protests by port workers refusing to show a Green Pass to get to work threatened to affect commercial activities, though early reports suggested the ports were operational. Protesters shouted "Liberta" (Freedom) in a largely peaceful demonstration in Florence. 
Implementation of the new requirement varies: Electronic scanners that can read cellphone QR codes with the Green Pass were set up at bigger places of employment, such as the office of Italian Premier Mario Draghi and the headquarters of state railway company Trenitalia. 
But at smaller places of work, from restaurants to tennis clubs, employers and managers had to download an app that can scan the codes. While it was unclear how strictly Italy would enforce the requirement, the fear of spot checks drove employers to comply, at least initially. 
Sanctions for employers who fail to check employees range from 400 to 1,000 euros. A worker who fails to show a Green Pass at work is considered to be absent without justification; if the worker shows up anyway without a valid Green Pass, he or she could face fines from 600 euros to 1,500 euros. 
CORONAVIRUS IN THE US: STATE-BY-STATE BREAKDOWN 
But there were some anomalies: Supermarket cashiers and hairdressers have to have a "Green Pass" to work, but their clients don't, and need only to wear a mask indoors. 
The aim of the requirement is to encourage even higher vaccination rates in a country that has kept the latest delta variant-fueled resurgence largely under control, reporting around 67 cases per 100,000 inhabitants and a daily death toll that hasn't exceeded 70 for months. 
In Italy, 80% of the population over age 12 has already been fully vaccinated. But for those people who can’t or won't get their shots, the expanded pass requirement imposes a burden of getting tested every 48 hours just to be able to go to work, though people with a proven medical condition that prevents them being vaccinated are exempt. 
Some employers are offering free tests at work, but the government has refused calls to make testing free across the board. Currently rapid tests run from 8 euros for children to 15 euros for adults. 
Testing capacity proved to be Italy’s Achilles’ heel during the first wave of the pandemic, and the governor of the Veneto region, Luca Zaia, has warned it won’t be able to keep up with the new demand. He has called for the government to let people secure Green Passes based on results from at-home test kits rather than having to go to a pharmacy for a rapid test. 
"If the law says people have the right to work with a test every 48 hours, they have to guarantee this right," Zaia said. 
TEXAS VACCINE MA

      An employee has her certification checked as Italy's new "Green Pass" vaccination requirement for employees to enter their offices became mandatory, at the Trenitalia, Italian train company offices, in Rome on Friday.
      (AP Photo/Andrew Medichini)
NDATE BAN TESTED BY DOD REQUIREMENT THAT FEDERAL CONTRACTORS IN STATE GET SHOTS 
Not even the Vatican was spared opposition to the new requirement: Three Swiss Guards quit and another three were suspended after they refused to get vaccinated before the Vatican’s green pass requirement went into effect. 
The Green Pass requirement is not a vaccine mandate, since a negative test or proof of being cured of COVID-19 are other ways to get it. In Italy, only health care workers are required to be vaccinated, and teachers and school administrators have had to have a Green Pass to work since Sept. 1. 
The Green Pass requirement for all categories of workers though went beyond other European countries. France has had a "virus pass" since the summer to access indoor activities and events, but it isn't required for employees to get into work. 

      An employee in Rome has her certification checked as Italy's new "Green Pass" vaccination requirement for employees to enter their offices became mandatory, at the Trenitalia, Italian train company offices on Friday
      (AP Photo/Andrew Medichini)
In Greece, employers are required by law to maintain a record of the vaccination status of staff who access work premises. Workers must carry a vaccination certificate that can be scanned using a government application or pay for weekly testing. 
In the U.S., the Biden administration imposed sweeping rules in September mandating all employers with more than 100 workers to require them to be vaccinated or test for the virus weekly, affecting about 80 million Americans. Another 17 million workers at health facilities that receive federal Medicare or Medicaid also have to be fully vaccinated, while vaccination is also required for employees of the executive branch and contractors who do business with the federal government — with no option to test instead. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
'Let the gourd times roll.' Zoo animals in Oregon chomp down on pumpkins in a top viral video of the day. 
The Smithsonian's National Zoo and Conservation Biology Institute vaccinated several of their primates against COVID-19 this week, saying it was just the beginning of animal coronavirus inoculations at its locations.
The zoo announced in a press release Friday that staff administered the first round of two-dose shots to 11 animals on Wednesday: seven orangutans, a western lowland gorilla, one white-eared titi monkey and two emperor tamarins.

      Apes wander inside their enclosure Jan. 4, 2018 at the Washington D.C. national zoo.
      (Andrew Lichtenstein/ Corbis)
ATLANTA ZOO TREATING 13 GORILLAS FOR COVID-19
A video posted by the zoo noted that the "animals were rewarded with honey for their participation."
The vaccine used was developed specifically for animals by Michigan-based veterinary pharmaceutical company Zoetis after the company saw that a dog in China contracted the virus early in the pandemic. 
Zoetis said in a press release in July that its shots were authorized on a "case-by-case basis by the United States Department of Agriculture" for an array of zoo animals, but said the shots are "not needed in pets or livestock at this time."
AUSTRALIAN RESCUE DOGS SHOT OVER COVID RESTRICTIONS: REPORT
The National Zoo also provided a status update on the lions and tigers under its care that had tested "presumptive positive" for COVID-19 last month, saying the big cats were "recovering well" and "behaving, eating and drinking normally."
"Vaccines will continue to be administered to select animals identified as susceptible species at the Zoo and at the Smithsonian Conservation Biology Institute in Front Royal, Virginia, in the coming months," the zoo explained, adding that "the lions and tigers will receive the vaccine no sooner than 90 days post-infection."
The National Zoo did not immediately respond to Fox News' questions regarding the inoculations.

      Tigers at the Smithsonian's National Zoo in Washington, DC. 
      (KAREN BLEIER/AFP)
Zoos in different parts of the country have increasingly been vaccinating myriad species with the Zoetis vaccine.
The Denver Zoo and Oakland Zoo used the jab on some of their animals over the summer, CBS News reported, and the Denver Zoo is planning to do the same.
FOX 35 reported Thursday that ZooTampa has also begun vaccinating its animals.
"Species such as Florida panthers, skunks, otters and primates are on top of the list to vaccinate," Fox 35 reported. "The zoo has received enough doses to vaccinate roughly 19 species which includes 93 animals."
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
'Fox Across America' host Jimmy Failla with reaction on 'Fox & Friends First.'
"Real Time" host Bill Maher railed against ongoing COVID restrictions, declaring the pandemic "over."
Maher kicked off the show's panel discussion Friday night by expressing relief that Dr. Anthony Fauci has given the green light on Halloween since it's been Maher's "position since the beginning of this."
"Just resume living," Maher told his audience. "I know some people seem to not want to give up on the wonderful pandemic, but you know what? It's over. There's always going to be a variant. You shouldn't have to wear masks. I should be to … I haven't had a meeting with my staff since March of 2020. Why?"
"I know some people seem to not want to give up on the wonderful pandemic, but you know what? It's over."

      ‘Blue states are a pain in the a--’ with their coronavirus rules, Bill Maher says. (HBO)
      
"Also, vaccine, mask, pick one! You've got to pick. You can't make me mask if I've had the vaccine," Maher added. 
BILL MAHER WARNS VIRGINIA DEMS: MCAULIFFE COULD LOSE ELECTION OVER SCHOOLS ISSUE BECAUSE ‘PARENTS VOTE’
The Atlantic staff writer Caitlin Flanagan told Maher she had "broken up with COVID" after the first year of the pandemic, comparing it to an "abusive" boyfriend. 
"And I got the vaccine. I walked out of the CVS. I hadn't been that thrilled coming out of the drugstore since I got the birth control pill in 1981," Flanagan quipped. "I've had cancer. I'm triple vaxxed. If it gets me, fair play to it because it will put up a fight against me but I'm not staying in my house again."
"I got the vaccine. … I hadn't been that thrilled coming out of the drugstore since I got the birth control pill in 1981."

      Caitlin Flanagan. (The Atlantic)
      
Maher then pressed his guest, Sen. Chris Coons, D-Del., since "it's the Democrats" that keep enforcing COVID restrictions. 
"I travel in every state now, back on the road, and the red states are a joy and the blue states are a pain in the a--. For no reason," Maher said. 
"One of the critical things that's being discussed right now by President Biden, one of the things we have to recommit ourselves to, is supporting vaccination around the rest of the world," Coons responded. "There's still a lot of countries that are very, very minimally vaccinated because if a variant develops out in the world that is able to defeat the vaccine, we are all the way back to the beginning. So in the United States, in most of the western world, we're ready to be done with this, but we're not done until the world is safe and we're not safe as a world until the world's vaccinated."
"If a variant develops out in the world that is able to defeat the vaccine, we are all the way back to the beginning."

      Sen. Chris Coons, D-Del., speaks on Capitol Hill in Washington, Thursday, Oct. 15, 2020. 
      (Associated Press)
BILL MAHER DEFENDS DAVE CHAPPELLE, KNOCKS CRITICS: ‘EVERYONE NEEDS TO NETFLIX AND CHILL THE F--- OUT’
"Except the world recognizes natural immunity. We don't," Maher pushed back, "because everything in this country has to go through the pharmaceutical companies. Natural immunity is the best kind of immunity. We shouldn't fire people who have natural immunity because they don't get the vaccine. We should hire them. Yes?"
"If someone is having tested with antibodies," Coons conceded. 
"Well, OK. But you know, people who've had it – I've had it," Maher said. "I mean, I shouldn't be tested anymore. I got the vaccine."
"And if someone's willing to be a fireman, if someone's willing to be a policeman, if someone's willing to go into a burning building and says, 'I'm just not that afraid of COVID and I don't want to take the vaccine,' that should be enough," Flanagan interjected. "You shouldn't be losing a job, you shouldn't be furloughed without pay, the guy that saves lives because he doesn't want to take the vaccine. It's ridiculous."
The HBO star complained about the "messaging" regarding COVID, pointing to people he had seen outside "alone walking with a mask," stressing "it's so stupid."
"It's an amulet, you know? A charm people wear around the neck that wards away evil spirits. It means nothing," Maher said. "I mean, can't we get people to understand the facts more?"
"It's an amulet, you know? A charm people wear around the neck that wards away evil spirits. It means nothing."

      iStock
      
Maher went on to slam Democrats over a poll that showed "41%" of them believed unvaccinated people have "over 50%" risk of hospitalization when it's actually "0.89%," adding that it's "0.01%" for vaccinated people. 
BILL MAHER SAYS US-MEXICO BORDER CRISIS MAY BE DEMOCRATS' ‘ACHILLES' HEEL' COME ELECTION TIME
"So in both cases, the correct answer is less than 1%. They thought it was over 50. How do people, especially of one party, get such a bad idea? Where did that come from?" Maher asked. 
Coons reiterated that "we frankly shouldn't let up on the urgency of still promoting vaccination" so that "we can enjoy reopening our society." 
But Maher pushed back on the lack of "consensus" on how many people have actually died from COVID, pointing to the recent passing of former Secretary of State Colin Powell, who Maher pointed out had cancer and Parkinson's disease but died of "complications from COVID."
"We're looking at people with complicated health histories a lot of the time," Flanagan said. "We're looking at obesity as an issue but no one wants to say it because it's body positivity. And we're looking at poverty. That's what we need to be focused on, people who live really close together. But there's a lot of people within different poor communities so don't want to take it. We just have to take our chances, be thoughtful and careful and go back out there and make sure that people who live in dense housing have complete access to the vaccine. And if they don't want to take it …"
Fox News medical contributor Dr. Marty Makary provides insight on 'Hannity' 
ORANGE, Calif. – Former President Bill Clinton remained in a California hospital early Friday after being admitted earlier in the week for a non-COVID-19-related infection.
"On Tuesday evening, President Clinton was admitted to UCI Medical Center to receive treatment for a non-Covid-related infection," Clinton's spokesman, Angel Urena, said in a statement on Thursday evening. "He is on the mend, in good spirits, and is incredibly thankful to the doctors, nurses, and staff providing him with excellent care."
University of California Irvine Medical Center in Orange, California, confirmed that Clinton was being treated there, Reuters reported.
The hospital is located about 45 miles from downtown Los Angeles. 
The former president, 75, was in Southern California to attend private events related to the Clinton Foundation, the Los Angeles Times reported. He was admitted to the hospital after feeling fatigued following a gathering with some friends in Orange County, the report said.
BILL CLINTON HAS A HISTORY OF SERIOUS HEALTH ISSUES
A source close to the situation told Fox News the former president was "diagnosed as a urological infection which morphed into a broader infection. As you can see in his statement from his doctors, the prognosis is good and they hope to have him home soon. He’s up and about, joking and charming the hospital staff."

      Former first lady and former U.S. Secretary of State Hillary Clinton, left, exits the University of California Irvine Medical Center in Orange, California, Thursday, Oct. 14, 2021. Former President Bill Clinton was admitted to the Southern California hospital Tuesday with an infection but he is "on the mend," his spokesman said.
      (Associated Press)
Clinton's infection is a type that is common among the elderly, Urena told the L.A. Times.
Just after midnight Friday, California time, former Secretary of State Hillary Clinton and her aide Huma Abedin were seen leaving the hospital and departing in a motorcade that was accompanied by local law enforcement vehicles. A Fox News reporter at the scene said Mrs. Clinton appeared also to be in good spirits, chatting with others as she exited the hospital.
Hillary Clinton was not in California on Tuesday when the former president was hospitalized, but she flew to California and attended a foundation event Thursday before visiting her husband at the hospital, the L.A. Times reported.

      The entrance to University of California at Irvine's Douglas Hospital in Orange, California, where former President Bill Clinton has been receiving medical treatment this week.
      (Fox News)
Urena released a joint statement from Doctors Alpesh Amin, chairman of the Department of Medicine at the University of California, and Lisa Bardack, director of Hospital Medicine for UCI Health.
"President Clinton was taken to UC Irvine Medical Center and diagnosed with an infection," the doctors wrote. "He was admitted to the hospital for close monitoring and administered IV antibiotics and fluids. He remains at the hospital for continuous monitoring."

      Hillary Clinton and aide Huma Abedin were seen in a motorcade that left University of California Irvine Medical Center in Orange, California, early Friday. Former President Bill Clinton has been undergoing treatment at the hospital since Tuesday.
      (Fox News)
"After two days of treatment, his white blood cell count is trending down and he is responding to antibiotics well," the doctors added. "The California-based medical team has been in constant communication with the President's New York-based medical team, including his cardiologist. We hope to have him go home soon."
Fox News' Edmund DeMarche contributed to this story.
Tyler O'Neil is an editor at Fox News. Follow him on Twitter at @Tyler2ONeil. If you've got a tip, you can email Tyler at tyler.oneil@fox.com.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Dr. Janette Nesheiwat on the importance of getting children 5 to 11 years old vaccinated when the FDA gives the green light 
The tide has turned COVID cases, hospitalizations, and the death rate are all on the decline. For the first time since August, the U.S. is now averaging under 100,000 new daily cases.
No longer are the days of hopelessness and no tools in our arsenal to fight COVID. I recall the days early in the pandemic when all I had was oxygen, inhalers, supportive care.
But now we are blessed. We have a variety of treatments and therapeutics that can truly save lives even if we do see another surge of cases during the winter holidays as we fast approach Thanksgiving and Christmas.
US SURGEON GENERAL: FDA LIKELY TO OK COVID-19 VACCINES IN YOUNGER KIDS AMID SCHOOL YEAR
The FDA is to meet October 26 to discuss pediatric vaccination safety and efficacy profile. In the meantime, Merck recently released data that its new antiviral pill Molnupiravir cut the risk of death and hospitalizations by 50 percent inthose with mild to moderate COVID.
This is incredible. The findings were so significant Merck halted its study to submit to the FDA because they know it can save lives. This is a major advance in the fight against this illness as it can help slow the spread of disease if started early and save lives plus it can be easily prescribed by a doctor.
But let's use it now. The FDA should swiftly grant EUA authorization as we still have more than 1,700 deaths across the country every day.
The beauty of Merck's new drug, Molnupiravir, is that it's a pill, not an IV drug. If prescribed you would take 1 capsule twice a day for 5 days. Similar to our flu treatment, called Tamiflu, that should be started within 48 hours of symptoms for most effectiveness.
There is one problem: the big price tag. It only costs Merck $17 to make a 5 day course yet charges $700. It's extremely expensive. Big Pharma knows we are desperate to save lives and end this pandemic.
I hope the price is negotiated down to avoid further health inequality and racial disparity. The beauty of this drug is that it can help in managing this disease and never allowing Covid or any disease result in lockdowns, school closures, loss of jobs, and loss of life.
And let's not forget the highly effective life saving monoclonal antibodies which reduce viral load and the severity of symptoms in addition to reducing the death and hospitalization rate by nearly 70 percent. If administered to high risk patients immediately after a Covid diagnosis it can reduce the risk of severe disease and death by nearly 80 percent. Remdesivir, Actemra, Decadron are all extremely useful medications to treat Covid.
To keep this trend of decreasing Covid cases and deaths moving in the right direction, it's important to understand risk and know how to protect yourself. Be aware of the prevalence of Covid in your community and protect yourself with vaccination if you haven't had recent infection which provides natural immunity for an uncertain length of time.
So, let's focus on the 65 million Americans eligible to be vaccinated. Only 55 percent of Americans are fully vaccinated. Let's increase testing, continue vaccinations efforts and boosters for those eligible with Pfizer but don't worry if you've had Moderna or Johnson & Johnson like I have. Data will probably come out soon allowing a mix and match of vaccines resulting in hybrid immunity. For example, if you've had J&J and you're a female under 50, it will probably be recommended you get a Moderna or Pfizer shot as your second dose. Don't forget for most, two doses of an mRNA vaccine is extremely effective in preventing severe disease and death.
Now last but not least, we can't forget about flu shots. Last year we had fewer than 1,000 deaths from the flu. Usually it's about 40k-60k deaths per year Why? because of the flu vaccine, mask use, and hand washing. The same precautionary measures used to prevent Covid apply to other diseases as well such as influenza, rhinovirus, RSV, strep, and more. 
Flu season is here. be sure to get your flu shot by the end of October. I am already diagnosing  cases of flu among my patients. You can have both Covid and flu together and that is dangerous and doubles your risk of death. But fortunately, that can easily be prevented.
We are on our way to ending this pandemic. We have "flattened the curve." The surge has peaked and is now on the decline. Let's keep it that way. We certainly don't want another spike in cases over the holidays and we now have the power to prevent that through vaccination, mask use, and routine testing. 
Know your risk. Protect yourself, your family, and your community.
Get the recap of top opinion commentary and original content throughout the week.
Subscribed
Florida Gov. Ron DeSantis says his state is trying to recruit law enforcement who are 'not being treated well' from other states amid vaccine mandates.
Florida Gov. Ron DeSantis argued on Sunday that coronavirus vaccine mandates "will wreak havoc in the economy."
The Republican slammed the vaccine mandates during an exclusive interview with "Sunday Morning Futures." 
"What Biden’s doing is unconstitutional. He does not have the authority to do this," DeSantis told host Maria Bartiromo. 
He then explained what the vaccine mandates will do on a "practical level." 
"In addition to be taking away people’s personal choices, it will wreak havoc in the economy because even if a small percentage of these folks end up losing their jobs or voluntarily walking away, you’re going to have huge disruptions in medical, in logistics, in law enforcement," DeSantis said. 
"So in Florida our policy’s very clear," he continued, "we’re going to have a special session and we’re going to say nobody should lose their job based off these injections." 
A White House spokesperson did not immediately respond to Fox News’ request for comment. 
DeSantis stressed that getting the vaccine is "a choice you can make, but we want to make sure we’re protecting your jobs and your livelihoods."
DeSantis made the comments three days after he tweeted out an updated version of the Florida state flag that was trending on social media after calling for the special session to ban local coronavirus vaccine mandates.
FLORIDA FINES COUNTY $3.5M FOR VIOLATING VACCINE MANDATE BAN
"Don’t tread on Florida," the flag reads with an alligator on the bottom paying tribute to the Gadsden flag that contains the message "Don’t Tread On Me."
On Thursday, DeSantis called on the Florida legislature to hold a special session with the aim of banning vaccine mandates in his state.
The Republican governor said he will convene a special session of the GOP-controlled statehouse in November to address vaccine requirements. He did not specify a starting date.
"At the end of the day, you shouldn’t be discriminated against based on your health decisions," he said during a news conference on Thursday. "We want to provide protection for people, we want to make it clear that, in Florida, your right to earn a living is not contingent upon whatever choices you’re making in terms of these injections."
DeSantis outlined policy goals for the special session, including holding businesses liable for adverse reactions to vaccines, removing legal liability protections for employers with vaccine mandates, and added protections for people fired for not being vaccinated.
PILOT REBUFFS BIDEN'S VAX MANDATE AMID SOUTHWEST TURMOIL: ‘WE HAVE ALL THE CONTROL’
The Florida governor also told Bartiromo that his state is "actively working to recruit out of state law enforcement" who risk losing their jobs unless they get the vaccine. 
Last week the Chicago police union’s first vice president, Michael Mette, issued a blistering attack on Mayor Lori Lightfoot’s vaccine mandate.  
Mette’s remarks were aimed at a city policy requiring that all city employees, including police officers, enter their vaccine status in the city’s data portal. 
On Tuesday, Police Superintendent David Brown said 21 department employees had been placed on "no-pay status" for refusing to provide the information. He said the department needed to talk to hundreds of officers who had thus far not provided the information. 
Mette encouraged those officers to stay their ground and blasted city leaders for not meeting at the bargaining table. 
"In Florida, not only are we going to want to protect the law enforcement and all the jobs, we’re actually actively working to recruit out of state law enforcement because we do have needs in our police and our sheriffs’ departments," DeSantis told Bartiromo. 
"So in the next legislative session, I’m going to hopefully sign legislation that gives a $5,000 bonus to any out of state law enforcement that relocates in Florida," he said.
On Sunday, DeSantis had a message for members of law enforcement: "If you’re not being treated well, we’ll treat you better here. You can fill important needs for us, and we’ll compensate you as a result." 
Earlier this month, DeSantis threatened to sue the Biden administration over the anticipated federal coronavirus vaccine mandate. Last month, the president announced businesses with more than 100 employees will be required to mandate COVID-19 vaccines or administer weekly tests. Employers are also required to pay employees for time off to get vaccinated and recover from side effects. 
The governor's comments came during a press conference in Fort Myers on monoclonal antibody treatments, which the governor has worked to make more accessible in the state to prevent severe COVID-19 infections.
"I think that the mandate is going to lose in court," DeSantis said during the press conference regarding the federal mandate.
He added that Florida would contest any such mandate from the Biden administration "immediately," and that any lawsuits from the state would be filed in the 11th Circuit Court of Appeals.
DeSantis and Biden have taken opposite stances on both vaccine and mask mandates. While the president issued a mask mandate on federal grounds soon after taking office, DeSantis barred local mask mandates in Florida.
Fox News’ Andrew Mark Miller, Bradford Betz, Audrey Conklin and The Associated Press contributed to this report. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Chicago Bears coach Matt Nagy says he has tested positive for COVID-19.
Nagy, who is vaccinated, announced the result during a Zoom call Monday minutes after his usual in-person session was switched.
"I feel pretty good," he said from his car.
Special teams coordinator Chris Tabor will run meetings that Nagy can't conduct virtually.
League rules say vaccinated individuals who are asymptomatic can return to the practice facility once they have two consecutive negative PCR tests taken at least 24 hours apart. If they are symptomatic, they need two negative tests taken at least 24 hours apart and must be symptom-free for 48 hours.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Researchers are studying whether certain biomarkers in saliva may help predict COVID-19 severity in children, according to the American Academy of Pediatrics. While most kids infected with COVID-19 typically have mild illness, some face serious complications like heart inflammation or respiratory failure. 
The team of scientists from Penn State College of Medicine and Wayne State University are collecting saliva samples from 400 COVID-19 patients ages 18 and under seeking emergency care at two children’s hospitals, the pediatrics group wrote in a release posted Thursday. Findings will be presented at the virtual American Academy of Pediatrics 2021 National Conference & Exhibition.
"Using saliva to predict severity of the infection is non-invasive and painless," Dr. Usha Sethuraman, study author and professor of pediatrics at Central Michigan University, said in the release. "If proven to be effective, saliva may be a game changer in children in whom obtaining blood is both difficult and distressing. Additionally, early recognition of the severity of COVID-19 can help clinicians institute timely and appropriate treatment which may help improve outcomes."
Sethuraman noted there aren’t any established biomarkers to predict disease progression among kids exposed to COVID-19.
Researchers are specifically studying cytokines and microRNAs, or biomarkers believed to control bodily inflammation upon infection. An early analysis among 150 kids indicated elevated levels of two cytokines (MIG and CXCL-10) among those with severe COVID-19 versus those without a serious course of COVID-19 disease, as well as altered microRNA levels, most of which were said to be "significantly lower" in kids with severe infection.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Former White House Press Secretary Ari Fleischer joins 'America's Newsroom' following the passing of Former Secretary of State Colin Powell.
Gen. Colin Powell, former secretary of state, died Monday at 84 years of age from COVID-related complications, even though he was fully vaccinated, his family announced. 
His death, medical experts say, underscores the need for COVID-19 vaccine booster shots among older adults and high-risk populations to shore up protection.
Powell was afflicted with other diseases, including Parkinson’s and the blood cancer multiple myeloma, which could hamper recovery from COVID-19 infection, according to reports. His family didn't specify when Powell received vaccine, or whether he had taken a booster shot.
Also, studies have shown that certain patients with weak immune systems don’t always elicit substantial levels of COVID-19 vaccine-induced antibodies, and regulators in August authorized a third dose of the Pfizer and Moderna COVID-19 vaccines for certain vulnerable patients, like solid organ transplant recipients, patients taking treatment for blood cancers or tumors, among other patients with conditions considered to have a similar level of immunocompromise, according to the Centers for Disease Control and Prevention (CDC).
COLIN POWELL, FORMER SECRETARY OF STATE, DEAD AT 84 FROM COVID-19 COMPLICATIONS
"The vaccines that we have, and he [Powell] evidently was fully vaccinated, are extraordinarily good against preventing death, hospitalization and severe disease but they are not perfect," Dr. Greg Poland, infectious diseases expert at the Mayo Clinic, told Fox News, adding that depending on patients’ age, gender and underlying medical conditions, up to 5% will not be fully protected.
"That is the very reason that we are engaging now in a national dialogue about booster doses," Poland said. Regulators last month authorized a booster dose of the Pfizer-BioNTech COVID-19 vaccine for adults ages 65 and older, and people ages 18-64 at high risk of exposure and severe COVID-19 disease. 
A Food and Drug Administration advisory committee endorsed a similar authorization for Moderna’s half-dose booster shot, and also recommended a second shot for all adults ages 18 and older who received the single-shot Johnson & Johnson vaccine at least two months ago. 
"The shot works. This is not evidence that the shot doesn’t work," said Dr. Marc Siegel, Fox News medical contributor and professor of medicine at NYU Langone Health. "This is an outlier but it’s a wake-up call for boosters."
Several medical experts, including Dr. Aaron Glatt, chair of the department of medicine at Mount Sinai South Nassau, told Fox News that older adults and high-risk populations should receive booster vaccines to increase their protection.
"If any good could come out of this, it’s a warning to all that booster doses have their place, particularly in the more elderly, or frail or people with underlying medical conditions," Poland said. "As soon as they can get their booster, they should."
Fox News' Brooke Singman contributed to this report.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News contributor Joe Concha on the New York Times overstating kids’ COVID hospitalizations.
Fox News contributor Joe Concha joined ‘America’s Newsroom' Monday blasting the New York Times for overstating kids’ COVID hospitalizations after the publication misreported upwards of 800,000 cases.
NEW YORK TIMES ISSUES MASSIVE CORRECTION AFTER OVERSTATING COVID HOSPITALIZATIONS AMONG CHILDREN
JOE CONCHA: 840,000 missed, right? Just incredible. Look, this is why trust in media is where it is. Gallup found that 7% of those polled have a great deal of trust in media. Even news organizations with well-paid editors and all these layers somehow allowed this misinformation from a biased reporter to get out into the public domain and go viral on social media alarming parents across the country, because this story did go viral. 
...
You know what didn’t? The limp correction. That’s how it works. The allegation gets 1,000 times more coverage than the correction. "The New York Times" was off by 840,000 hospitalizations of children with Covid. Plus, and this is very important, by the way. There is no accountability. The reporter in the piece once declared that the Wuhan lab leak theory was based in quote racist roots unquote, and now another Covid story, she gets wrong… You have to wonder at this point are these mistakes being driven by a motive to push a narrative of fear? 
WATCH FULL VIDEO BELOW:
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Delta COVID-19 variant increases the risk for complications among unvaccinated pregnant women, a recent study found.
The study, published in American Journal of Obstetrics and Gynecology, analyzed the trend of severe COVID-19 illness among pregnant women as the highly transmissible delta variant rose to become the predominant strain.
From May 2020 to September 2021, 1,515 pregnant women were diagnosed with COVID-19 at a Dallas public health system, including 82 severe cases (81 among unvaccinated patients) and 11 requiring mechanical ventilation. Study authors reported two maternal deaths.
COVID-19 VACCINATION AMONG PREGNANT WOMEN REMAINS LOW DESPITE SEVERE RISK
Results indicated that around 5% of pregnant patients battled severe COVID-19 until around March 2021, and before increasing to 10-15% by summer’s end, amid a delta-driven surge.
Dr. Emily Adhikar, an assistant professor of obstetrics and gynecology at University of Texas Southwestern Medical Center and lead researcher on the study, told the Dallas Morning News of concerns over future implications for pregnant women who have yet to receive a COVID-19 vaccine. 
"I am concerned about what the future holds for pregnant women who have not been vaccinated," Adhikari told the outlet. "We have experienced sicker patients with this last variant, so it means we have to vaccinate as many people as possible."
The study concluded that pregnant women diagnosed with the delta variant were more likely to have severe disease and those who were also unvaccinated were more likely to be hospitalized. Dr. Aaron Glatt, an infectious disease specialist and a spokesman for the Infectious Diseases Society of America, who was not directly involved with the study, told Health Day: "If you’re pregnant and you get COVID-19, you’re at increased risk of becoming severely ill."
Researchers urged pregnant women to get vaccinated as the best method to prevent COVID-19. Last week, the Centers for Disease Control and Prevention (CDC) issued a health alert urging pregnant women or those trying to become pregnant to get vaccinated for COVID-19.
As of Sept. 27, 2021, CDC data indicate over 125,000 laboratory-confirmed COVID-19 cases in pregnant women, 22,000 of which resulted in hospitalization, with 161 deaths. Despite the severe risk, the CDC reports that only about 31% of pregnant women ages 18 to 49 are fully vaccinated against COVID-19.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News medical contributor Dr. Janette Nesheiwat discusses booster shots, Moderna and Johnson & Johnson alternatives, and new CDC, FDA guidance
A new British study has determined it is safe to administer flu and COVID-19 vaccines at the same time.
Researchers administered either a flu shot or a COVID-19 vaccine to adults at one of 12 sites across Britain. Three weeks later, those who received a flu shot then received a COVID-19 vaccine shot and vice versa – though some received a placebo shot. 
COVID-19 VACCINATION AMONG PREGNANT WOMEN REMAINS LOW DESPITE SEVERE RISK
The study, which followed 340 participants in randomized trials, found "no safety concerns" from administering both shots and that both vaccines maintained the appropriate immune response, according to a preprint of the study in medical journal The Lancet. 
"Most reactions were mild or moderate," the study noted. "Rates of local and unsolicited systemic reactions were similar between randomized groups." The study reported only one "adverse" event that resulted in hospitalization but highlighted that "immune responses were not adversely affected." 
LAST YEAR'S HEROES, THIS YEAR'S SCAPEGOATS: FRONTLINE WORKERS LIVELIHOODS AT STAKE OVER VACCINE MANDATES
Researchers from The University of Bristol, University of Oxford and University Hospitals Bristol and Weston NHS Foundation Trust conducted the full trial over six weeks. All subjects were given the age-appropriate shot for each vaccine. 
Dr. Rajeka Lazarus, lead scientist and a consultant in infectious diseases and microbiology at University Hospitals Bristol and Weston NHS Foundation Trust, noted the results required peer review, but she stressed that it is "a really positive step." 
NURSING PROGRAMS STRUGGLE TO KEEP UP AMID A NATIONWIDE SHORTAGE OF NURSES
The study indicates that hospitals can reduce the number of appointments for patients as they look to administer booster shots and flu shots ahead of the winter season, which last year presented a significant rise in COVID-19 infections as people remained indoors during the colder weather. 
Around 97% of the subjects said they would willingly receive two vaccines at the same appointment after the study, The Guardian reported. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
As temperatures cool and students return to classrooms amidst the ongoing COVID-19 pandemic, flu season has arrived once again.
Officials are urging Americans to get their shots and U.S. Centers for Disease Control and Prevention (CDC) Dir. Rochelle Walensky said last week that while she knows people are "tired of talking about vaccines," it is still "doubly important this year" to get a shot.
FAUCI SAYS COVID-19 PANDEMIC UNCONTROLLED AS 66M REMAIN UNVACCINATED
Flu cases have dropped to historically low levels during the pandemic, with coronavirus restrictions blocking other respiratory viruses. 
However, with schools and businesses reopened, there is no telling how bad a flu season the U.S. can expect this winter and officials are worried because a different respiratory virus – RSV – came back last summer.
Annual flu vaccinations are recommended for just about everybody, starting with six-month-old babies. 

      FILE - In this Thursday, Jan. 23, 2020, file photo, a patient receives an influenza vaccine in Mesquite, Texas. Amid all the focus on COVID-19 vaccinations, U.S. health experts have another plea: Don’t skip your flu shot.  With U.S. schools and businesses reopened, international travel resuming and far less masking this fall, flu is likely to make a comeback. 
      (AP Photo/LM Otero, File)
Influenza is most dangerous for adults over age 65, children under age five, people with chronic health problems and pregnant people.
The CDC encourages people to get their vaccines by the end of October. 
Last fall, about as many Americans overall got their flu vaccination as they did prior to the pandemic: about half of the eligible population.
The CDC expects vaccine makers to deliver 188 million to 200 million doses of flu vaccine, which most Americans with health insurance can get without a co-pay. A record nearly 194 million doses were distributed last winter.
Options include regulars shots and a nasal spray and all offer protection against four different flu strains that experts predict are the most likely to spread this year.
Officials have also urged older adults and those with chronic illnesses to inquire about getting a vaccine against a type of pneumonia that is a frequent complication.
In addition, the CDC says it is also OK to get a flu vaccine and a GOVID-19 vaccine at the same time.
Flu, a contagious respiratory illness caused by influenza viruses, infects the nose, throat and lungs. 
The CDC notes that while the flu can cause mild to severe illness, it can sometimes lead to death.
Flu symptoms include fever, chills, cough, sore throat, runny or stuffy nose, muscle or body aches, headaches, fatigue and some people may having vomiting and diarrhea.
About 8% of the U.S. population gets sick from the flu each season, the CDC says, with a range between 3% and 11% depending on the season.
While there are influenza antiviral drugs that can be used to treat the flu, the agency says the drugs are not a substitute for the vaccine: the best way to help prevent seasonal flu and its potentially serious complications.
The Associated Press contributed to this report.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
The ‘Outnumbered’ panel reacts to protests over vaccine mandates in New York City and CDC Director Walensky’s comments about education for the unvaccinated
New York City municipal employees are marching across the Brooklyn Bridge Monday against the COVID-19 vaccine mandate.The protest, which is set to end in front of City Hall on the Manhattan side of the bridge, is billed as an anti-mandate protest on behalf of nearly 50,000 NYC employees who have yet to be vaccinated with a deadline just days away.Traffic is shut down on the Brooklyn Bridge into Manhattan as of 11:49 a.m., according to police.
NYC'S BARCLAY'S CENTER SWARMED BY PROTESTERS SUPPORTING NETS' KYRIE IRVING'S REFUSAL TO BE VACCINATEDPIX11 reports all city workers must have their first shot of the coronavirus vaccine by 5 p.m. Friday if they want to come to work the morning of Nov. 1.Monday's protest follows a protest Sunday night at the Barclay's Center in support of Kyrie Irving. A crowd of people rallied as the Brooklyn Nets lost to the Charlotte Hornets at their home opener without their point guard. At one point the protest turned violent when some demonstrators tried to break into the arena, clashing with security and police.Irving has refused to get vaccinated. As a result, he's not getting paid. The same could soon be said for thousands of city workers if they don't get the shot by Friday.That's the threat from Mayor Bill de Blasio with vaccination rates lagging behind the general population at several large city agencies including the NYPD and the FDNYP.NEW YORK CITY POLICE UNION THREATENS LEGAL ACTION OVER DE BLASIO VACCINE MANDATE"It's time now. If you don't want to get vaccinated, you'll be put on unpaid leave. Well, the vast majority of human beings go to work to get paid. And also, I think for a lot of our first responders, there's a calling. They believe in the work, they care about the work. Those two factors I think are going to cause the vast majority to get vaccinated," Mayor de Blasio said.
Pilar Arias is a multimedia journalist with more than 10 years of experience in broadcast, digital and print production. She enjoys covering a wide variety of topics. Follow her on Twitter: @PilarFOXNews.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Journalist dishes on America's indispensable role in the development of COVID-19 vaccines on 'Fox News Primetime.'
Journalist Gregory Zuckerman called the development of a COVID-19 vaccine "an American story" Thursday on "Fox News Primetime."
Moderna was "developing a vaccine for years and people counted them out" because of its mRNA approach to vaccines, the "A Shot to Save the World" author said. The company persisted despite skepticism from experts.  
CEO Stéphane Bancel "had a vision [for a vaccine] and he kept pushing [his employees]. And that's in some ways an American story [of] American entrepreneurs," Zuckerman said.
MODERNA SAYS LOW-DOSE COVID-19 VACCINE IS SAFE AND APPEARS TO WORK FOR KIDS AGE 6-11
The author said he contacted entrepreneurs, executives, investors and scientists - "mostly American" - as the vaccines were being developed because he had bet on COVID vaccines being "successful and effective." 
"There was American exceptionalism, I would argue, in terms of both the investors, but also the scientists working deep in these labs[,]…working hard and trying to develop the vaccines," he said.
According to Zuckerman, foreign CEOs "say without America, these vaccines could not be done" without American scientists and investors who bankrolled development "with just the promise of potential profits down the road. Only in America could that happen."
FILE PHOTO: Walmart pharmacist holds a vial of the Moderna coronavirus disease (COVID-19) vaccine inside a Walmart department store in West Haven, Connecticut, U.S., February 17, 2021. REUTERS/Mike Segar/File Photo ( )
U.S. President Donald Trump signs an executive order on vaccine distribution during an Operation Warp Speed Vaccine Summit at the White House in Washington, U.S., December 8, 2020. REUTERS/Tom Brenner ( )
FILE PHOTO: A woman holds a small bottle labeled with a "Coronavirus COVID-19 Vaccine" sticker and a medical syringe in front of displayed Novavax logo in this illustration taken, October 30, 2020. REUTERS/Dado Ruvic/File Photo ( )
What former President Donald Trump called a "safe and effective vaccine" was achieved in only nine months under his Operation Warp Speed in what Zuckerman deemed a "modern-day miracle."
When asked by host Brian Kilmeade about "unsung heroes" of vaccine development, Zuckerman spotlighted Novavax, a small Maryland company. He said it was "on [its] last legs" in early 2020, with its stock price at $3.93 on Jan. 10, 2020, it closed at $150.62 on Thursday.
"Everyone counted them out," he continued, but "they kept at it and…ignored all the skepticism." Zuckerman expects Novavax's vaccine to be approved "soon" for worldwide distribution.
Graham Colton is an associate editor for Fox News Digital.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Chicago Bears coach Matt Nagy will miss Sunday's game against San Francisco because of the NFL’s COVID-19 protocol.
The team announced Saturday that special teams coordinator Chris Tabor will serve as head coach against the 49ers.
Nagy said Monday he had tested positive for COVID-19. The 43-year-old coach, who is vaccinated, announced the result during a Zoom call minutes after his usual in-person session was switched.
Chicago (3-4) had four players on the COVID-19 list for last weekend’s 38-3 loss at Tampa Bay, with linebacker Caleb Johnson and right tackle Elijah Wilkinson joining star linebacker Robert Quinn and veteran tight end Jimmy Graham before kickoff. Running back Damien Williams was removed from the list a day before the game.
Former secretary of state weighs in on foreign threats facing the U.S. on 'Hannity'
The Biden administration’s mounting Afghanistan, immigration, and spending woes threaten to obscure its failure to hold Beijing accountable for the deceptions that sped the spread of SARS-CoV-2 into an unsuspecting world.   
Yet, as widely acknowledged, we ignore at our peril the Chinese Communist Party’s (CCP) staggering wrongs. Prudence requires America and its allies adopt a more responsible and comprehensive course. 
MIKE POMPEO ISSUES STARK WARNING AFTER CHINA FIRES NUCLEAR-CAPABLE HYPERSONIC MISSILE
The CCP’s cover-up continues as do the mounting costs to Americans this past week surpassing 700,000 deaths.
The loss of American credibility following the Afghanistan debacle heightens the urgency for an American response to foreign bad actors, and Americans should demand one.   
We don’t need to reinvent international law. Just and well-established principles of international law require China fully compensate states it has wronged. 
For over 40 years, the U.N.’s International Law Commission studied international cases on just these principles. 
In 2001, the Commission captured its holdings in its "Articles on State Responsibility for Internationally Wrongful Acts."  The U.N. General Assembly, with China’s support, promptly commended this effort.  American and foreign courts have approvingly cited these standards and the Articles hundreds of times. 
These established international principles hold a state liable, for example, even if local officials perpetrated the wrongs.  
The loss of American credibility following the Afghanistan debacle heightens the urgency for an American response to foreign bad actors, and Americans should demand one.   
Beijing’s failure to fulfill its agreed international obligations to report promptly and honestly on Covid-19’s dangers alone justifies holding it responsible, as noted by Harvard Law School Visiting Professor James Kraska. 
CCP responsibility only increases for its continuing efforts to deceive the world.  If, as we believe, it recklessly engineered the virus and allowed its escape, International law provides an enforceable remedy for their evil.
WHITE HOUSE MUM ON REPORTS OF CHINA TESTING NUCLEAR MISSILE, SAYS ADMIN WELCOMES ‘STIFF COMPETITION’
The need to hold Beijing accountable for its misdeeds has been building for years; the CCP’s defiance of its SARS-CoV-2 responsibilities magnifies the stakes and immediacy.  As the CCP ’s economic and military might gains on the US, Beijing grows more brazen.  In recent months, a CCP-guided publication threatened Japan with nuclear annihilation and dismemberment. In violation of international obligations, Beijing accelerates efforts to extinguish Hong Kong’s freedom, militarize illegal South China Sea bases, and weaponize unfair practices to dominate trade and supply chains. 
The pandemic has fueled Beijing’s drive for a world suiting autocratic repression by distracting America and increasing China’s relative economic rise.  Beijing now openly prioritizes gaining the capability to cripple other states’ economies while remaining invulnerable itself. 
REP. GALLAGHER: THIS SHOULD BE BIDEN'S 'SPUTNIK MOMENT' ON CHINA AGGRESSION
Extensive PRC investments – for example, in its dual circulation model, Belt and Road Initiative, and sanction-proof digital Yuan – further that worrisome aim. CCP General Secretary XI has defiantly proclaimed that a wall of steel faces those in Beijing’s way. 
So far the democracies have not imposed costs for CCP wrongs greater than the benefits Beijing derives. Such forbearance has not slowed and may have paved Xi’s aggressive ways. 
Recognizing the PRC as an ill-intentioned state, the democracies should not be tolerant of wrongs that fuel its rising aggressions.  The PRC claws for such advantages.  The CCP’s SARS-CoV-2 malfeasance cannot be airily -- and foolishly -- dismissed as affecting only far-off people, isolated rocks in a distant sea, or multi-national corporations that should protect themselves. 
NBC FACT-CHECKS FAUCI'S FEAR THAT COLLEGE FOOTBALL GAMES WOULD BE COVID SUPER-SPREADERS: 'NEVER HAPPENED'
The virus stalks our streets and cripples our economy. To this day, the CCP defies without consequence even international inquiries into Wuhan’s practices. We do not wish to see another virus wing its way from Wuhan.
Diplomatic and lawful measures jointly taken with our allies hold the best prospects for achieving a measure of justice and for tempering Xi’s aggressive path.  Under the Articles and accepted international principles noted above, injured states are allowed to impose countermeasures and selectively suspend obligations to the wrongdoer until fully compensated. 
Such efforts should hold Beijing and, as appropriate, its state-controlled entities liable for Covid-19 wrongs and other widely recognized misdeeds, including IP theft.  Many support the U.S. and allies sanctioning CCP officials directly involved, or higher officials more generally, and curtailing visas, scientific exchanges and grants.  These are worthwhile measures, rightly pursued. 
Sadly, these measures alone are not proportionate to the harm the CCP has caused and do not compensate victims.  Broader diplomatic demands, international countermeasures, and legal actions are needed, as well. 
U.S. and international preferences granted China when it was less developed and better behaved should also be curtailed. For example, the U.S. should end its practice of granting PRC companies preferred treatment in our capital markets.  These fuel CCP plans and risk Chinese defaults endangering our economy.  PRC entities should meet the same audit and reporting standards that govern U.S. companies. 
Immunities granted to foreign sovereigns were not adopted to protect grossly illegal activities, such as sending deadly agents into America.  Obtaining just results could be facilitated by the Biden Administration and, as needed, by amendments that still protect legitimate sovereign discretion. 
Crucially, targeted investments in US and allies’ military capabilities, technological advances, export controls, strategic communications, and counters to Beijing’s anti-competitive market practices are overdue.  Beijing wants Asia and then the world to sleep-walk into Xi’s authoritarian hegemony. We should not oblige.
Xi’s CCP will retaliate harshly to any corrective measures, especially substantial ones.  It will hurl unjust charges, sanction companies, and seize Americans.  Artful diplomacy can mitigate but not eliminate these costs. Beijing needs the world economy; its retaliation will be lessened if other democracies rally to this cause. 
Perhaps fear of trumped-up PRC retaliation will deter President Biden. The CCP may then fairly ask, if hundreds of thousands of dead fail to move America and the world, what would?  We will bear the consequences of today’s neglect.
No democratic state would have acted as irresponsibly as Beijing. 
What does Beijing’s brazen, on-going malfeasance regarding SARS-CoV-2 say about that regime’s future course? And, if we fail to act, what does that say about us?   
Lewis Libby is senior vice president of Hudson Institute. He guides the Institute’s program on national security and defense issues, devoting particular attention to U.S. national security strategy, strategic planning, the future of Asia, the Middle East, and the war against Islamic radicalism.
Mike Pompeo is a Fox News contributor, former U.S. secretary of State, and former director of the Central Intelligence Agency. He is a distinguished fellow at the Hudson Institute.
Get the recap of top opinion commentary and original content throughout the week.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Americans drank and smoked more during the course of the COVID-19 pandemic, researchers say.
In a new study published in the peer-reviewed journal Nutrients, a national team led by the University of California, Los Angeles found that U.S. residents also spent less time exercising and more time in front of a screen.
"We found that regulations to restrict non-essential activities and stay-at-home orders during the pandemic have had profoundly negative impacts on multiple lifestyle behaviors in American adults," Dr. Liwei Chen, UCLA Fielding School of Public Health associate professor of epidemiology and lead author of the study, said in a UCLA release. "As bad as these changes have been for all Americans, they disproportionately impact racial and ethnic minorities in the U.S., who already bear a higher disease burden from COVID-19."
DEPRESSION, ANXIETY FELL AS US COVID-19 RESTRICTIONS ENDED IN 2021: CDC DATA
In order to reach these conclusions, the authors conducted a survey called the Health, Ethnicity, and Pandemic (HEAP) Study in October 2020 among adults. 
The HEAP Study was funded by the Center for Reducing Health Disparities at the University of Nebraska Medical Center, The Chinese Economists Society and the Calvin J. Li Memorial Foundation. The study was designed by investigators from several universities and carried out by the National Opinion Research Center (NORC) at the University of Chicago. 
Participants of the study were selected using 48 sampling criteria, including age, race, ethnicity, education and gender. 
Those selected – more than 2,700 – were asked to report five lifestyle behaviors before and during the pandemic, including exercise time, screen time, fast-food meal consumption, alcohol drinking and cigarette smoking.

      A man smokes a cigarette outdoors
      (iStock)
The relation of social and demographic factors with each lifestyle change was estimated using "weighted multivariable logistic regression models."
Across those surveyed, the time spent on exercise decreased by more than 31%, screen time increased by more than 60%, alcohol consumption increased by more than 23% and smoking increased by 9%. 
That said, the average consumption of fast food dropped from 1.41 times per week to 0.96 times per week during the pandemic.
"The observed decrease in fast food consumption is likely due to the stay-at-home order and the closure of fast-food restaurants during the pandemic," Chen said. "Although the majority of our study’s participants, about 77%, reduced or did not see a change in their fast-food meal consumption, there were still almost 23% that increased how much fast food they ate in the same period."
PEOPLE ARE TURNING TO HORSE THERAPY TO IMPROVE MENTAL HEALTH DURING THE PANDEMIC
The authors also identified subgroups that were more vulnerable to adverse influences from the pandemic, 
Compared to Non-Hispanic Whites, Non-Hispanic Blacks and Hispanics were more likely to have undesired changes in multiple lifestyle behaviors, including exercise, screen time, fast food intake and alcohol consumption. 
American Indians and those in the "other" racial category were more likely to decrease their exercise time and increase consumption of fast-food meals and Asian Americans were less likely to increase alcohol drinking and cigarette smoking. 
The findings, the authors said, were consistent with those from previous studies that documented the disproportionate exposure to and suffering from the COVID-19 pandemic by these groups.
In addition, younger-aged adults were also more likely to have undesired changes in exercise time, consumption of fast-food meals, alcohol drinking and cigarette smoking, compared with old adults. 
Women had higher odds to increase screen time during the pandemic and married individuals were not more likely to decrease exercise time than those who were married or lived with partners.
Lower odds of smoking during the pandemic were associated with higher household income and individuals with higher education levels had higher odds of having more undesired lifestyle changes including less exercise time, more screen time and more alcohol drinking.
Notably, the study has several limitations including that survey data was only collected at the one-time point during the pandemic and that limited information was collected for each lifestyle behavior due to the concerns regarding participant time and burden. 
For dietary intake, the researchers solely focused on the consumption of fast-food meals.
Nevertheless, the authors say that mitigating the impacts of COVID-19 requires effective interventions.
"We found a marked increase in sedentary behaviors, alcohol consumption, and cigarette smoking, and a decline in exercise," Dr. Jian Li, Fielding School professor of environmental health sciences and a co-author, said in the release. "Whether these persisted as the pandemic continued, and whether individual’s quality of life and health well-being are subsequently affected, has to be studied, but it is clear that resources and support that can help people maintain healthy lifestyles, during the pandemic and afterwards, are urgently needed."
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Memory loss and "brain fog" may be long-term side effects of COVID-19, according to researchers. 
In a recent study published last week in the journal JAMA Network Open, Mt. Sinai Health System experts analyzed data from 740 participants – some of whom had contracted the virus and some who had only received a COVID-19 vaccine.
DEMENTIA SIGNS ARE IN THE BLOOD, RESEARCHERS SAY
The average age of the patients – who had no history of dementia – was 49 and 63% were women. The mean time from COVID-19 diagnosis was nearly eight months and the majority of those studied were White. 
In order to measure the prevalence of post-COVID-19 cognitive impairment and its association with the severity of the disease, the team analyzed patient data from April 2020 through May 2021.

      Health care workers during an intubation procedure to a COVID-19 patient.
      (iStock)
Patients who had been treated in outpatient, emergency departments or inpatient hospital settings reported their own demographic characteristics.
Cognitive functioning was tested using "well-validated neuropsychological measures," including counting forward and backward, a language test and the Hopkins Verbal Learning Test that showed the patients a series of words in different categories and tested how many they could recall.
MILDER COVID-19 INFECTION COULD STILL LEAVE BRAIN WITH LASTING IMPACT: UK STUDY
Next, the researchers calculated the frequency of impairment on each measure and they used logistic regression to assess the relationship between cognitive impairment and COVID-19 care site – adjusting for race and ethnicity, smoking, body mass index, comorbidities and depression. 
In all, they found that the most prominent cognitive deficits were in both memory encoding and memory recall, which showed up in 24% and 23% of the participants, respectively.
Additionally, hospitalized patients were more likely to have impairments in attention, executive functioning, category fluency, memory encoding and memory recall than those in the outpatient group. Those treated in the emergency department were also more likely to have impaired category fluency and memory encoding than those treated in the outpatient setting.
"The relative sparing of memory recognition in the context of impaired encoding and recall suggests an executive pattern," the researchers wrote. "This pattern is consistent with early reports describing a dysexecutive syndrome after COVID-19 and has considerable implications for occupational, psychological, and functional outcomes."
The group also noted that while it is well-known that older adults and certain populations may be particularly susceptible to cognitive impairment after critical illness, a substantial proportion in the relatively young cohort in the study also exhibited cognitive dysfunction several months after recovering from COVID-19. 
The researchers said that further studies were needed to identify risk factors, mechanisms underlying cognitive dysfunction and options for rehabilitation.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
A San Antonio mom has given birth to two healthy baby girls despite testing positive for COVID-19. 
Wendy Leal’s family said they were uncertain for weeks whether the twins would make it. 
"We thought, ‘oh my god, what’s going to happen with the girls," Leal’s sister, Yessica Trevino, told San Antonio’s KENS 5. 
Trevino said the virus took a toll on her sister, who is unvaccinated. 
TEXAS GOV. GREG ABBOTT BANS ‘ANY ENTITY’ FROM ENFORCING A COVID-19 VACCINE MANDATE
"She was sick and it was hard for her to talk and stay," Trevino told the station. "Me in particular, I never heard someone being pregnant with COVID and everything was good. So yes, we were concerned that the girls wouldn’t make it." 
Doctors performed an emergency C-section and Leal gave birth to twins, Matilde and Renata, last Monday. She was with them only for a moment before they were separated. 
"Thank God they didn’t catch anything," Trevino said. "We’re just waiting for (the doctors) to tell us when they can get out."  
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News host gives his take on Australian government's handling of the COVID-19 pandemic and the protests that have ensued because of it on 'Tucker Carlson Tonight'
One thing about Americans: they love Australia. Most Americans have never been there. It’s an awfully long way away. But when Americans think of Australia, they imagine a freer, tougher version of themselves. Steve Irwin, Crocodile Dundee, that kind of thing. So there’s a huge reserve of affection in the United States for Australia, its culture, and its people. It’s also possible most Americans, us included, have not updated our assumptions about Australia in a while. The modern reality is a little different from what we imagine.
Case and point: In June of 2019, federal police in Sydney, Australia raided the offices of the state broadcaster, ABC. They weren’t at all unclear about why they were raiding the offices. They said it out loud. Just days before the raid, ABC broadcast allegations from a whistleblower that embarrassed Australia's government. This whistleblower said that Australia's military leaders had killed civilians in Afghanistan, including children, and had lied about it. ABC broadcast that story. 
It wasn’t a crime to broadcast the story, and Australia’s federal police didn’t pretend it was. Instead, they served ABC with a warrant that authorized them, the police, to cover up the evidence of the military's misconduct. The warrant, and we're quoting, allowed police to "add, copy, delete, or alter" any material they wanted to alter on the broadcaster's computers. 
That’s not the kind of thing that happens in a free country, to put it mildly. And yet, Australia's military and police forces never suffered any consequences for doing it; In fact, many Australians supported it. They rewarded their military with hundreds of millions of dollars in new spending -- most of that money was intended to keep Australians safe from the malign influence of "Chinese authoritarianism," even though that seemed a lot like Chinese authoritarianism itself.  
MEDIA STOPS COVERING FL COVID DATA BECAUSE DESANTIS' DOWNTREND THREATENS LOCKDOWN POLITICS: SEXTON, TRAVIS
Two years later, what does Australia look like? It looks a lot like China did at the beginning of the pandemic. We showed you those images from China at the time -- the people being welded inside their apartments to starve, the guys in hazmat suits forcing people in quarantine boxes and driving away to some unknown destination. At the time, our public health officials, including Tony Fauci, told us nothing like that could ever happen in our country or in the west. But that was wrong because those things are now happening in Australia. This is what happens in Australia if you try to leave your apartment:
REPORTER: Anthony Karam knows he’s COVID positive when he steps into this public lift. Already breaking so many rules, he doesn’t bother to cover his mouth as he sneezes and splutters. The 27-year-old is still infectious but has gone missing from his Wentworth Point apartment, the warrant now issued for his arrest. 
HEALTH MINISTER BRAD HASSARD: This 27-year-old chap who apparently has expressed the view that he doesn’t care less whether he spreads the virus is one example of the worst of the worst.
So a national manhunt for a man who sneezed in an elevator. That’s the state of play in modern-day Australia. Not everyone in the country is on board with this, but since Australians were completely disarmed by their government several years ago, there’s precisely nothing they can do about it, so it’s accelerating. Look at what’s happening now. They’re being crushed. The scene in Melbourne (the second-most populous city in Australia) over the past month was chaos.
Is the government cracking down on Islamic extremists, dangerous revolutionaries in their midst? No. Just ordinary Australians complaining, demonstrating peacefully against the lockdowns, beaten by police.
You've seen a lot of footage from Australia that shows the chaos, but something that's not immediately obvious from the American vantage is this is not all of Australia. The whole country is not locked down. In Australia, most of the lockdowns are in the eastern part of the country, that’s where the capital of the country is and where the federal government has the most control. Western Australia, home to most of the country's national resources, isn't locked down at all. 50,000 fans just crowded inside a stadium for a rugby match in Perth, the capital of Western Australia; no one beat them with nightsticks or hosed by the police. The rugby match was not a super-spreader event. Western Australia has virtually no COVID cases.
 POLITICO REPORTER SCOLDS GOLD STAR FAMILY OF MARINE KILLED FROM KABUL ATTACK FOR NOT WEARING MASKS IN CAPITOL
How did that happen? How does Western Australia not lockdown but remain virtually COVID-free? Simple. By controlling its borders. Western Australia didn't allow thousands of people to stream in from anywhere they wanted to in the world. They’re not Texas. They didn’t care about protecting their borders. They’re not worried about being called racist. It seemed common sense, and it worked. 
And here's the really revealing thing. Australia's federal government is angry that Western Australia has closed its borders. They want that part of the country to open its borders. Why might that be? According to ABC News, Australia's government is, "arguing that [Western Australia's] internal border restrictions are a drag on the national economy." 
That’s interesting because the problem with Australia's economy does not come from Western Australia closing its borders. It comes from the lockdowns. Those are the biggest drag on the national economy ever conceived in Australia. So are those police SWAT teams beating people for going outside. 
COVID mandates are a far greater threat to Australia’s economy and its social fabric than COVID itself. The Queensland health minister, in eastern Australia, explaining that outdoor mask mandates are necessary because of two new COVID cases. Not two thousand, but two:
QUEENSLAND HEALTH MINISTER YVETTE D'ATH: What these two cases mean is that we will be extending immediately the directive in relation to mask-wearing to the Gold Coast. 
We want to pause for a moment to give you a sense of the scope of the pandemic in Australia: To date, COVID has caused 1,300 "recorded deaths" in the entire country. Australia has 25 million people. That 1,300 figure includes people who "died with probable COVID," whatever that means. 
In Alberta, Canada, the health minister just announced that anyone who stays home from any illness will be counted by the Canadian government as a COVID patient. Then she pretended she didn't say that because it’s obviously insane, but it’s on video, so we know she did.
In Australia, the government has adopted a similar standard -- anyone who leaves home is apparently being counted as a COVID patient. A man in Melbourne on Sunday made the mistake of walking outside a block from his home:
WOMAN: He lives a block away! 
POLICE OFFICER: He has no reason to be here. He has no valid reason to be out today.  He wasn’t wearing a face mask. 
WOMAN: He has a face mask in his pocket. He was just smoking a cigarette. He just came to get lunch with me. 
MAN: And the reason I didn’t have a mask on was I was having a cigarette. I have two masks in my pocket. What do you want me to do?
Here’s the interesting thing – apart from that’s obvious authoritarianism, it’s terrifying that could happen in a civilized English-speaking country, Australia of all places – notice the police didn’t ask the man if he’s been vaccinated. You think that’d be the first question they’d ask. Vaccination works, doesn’t it? That’s why it’s mandatory, right? 
REP. CHIP ROY INTRODUCES LEGISLATION TO BLOCK FINES FOR BIDEN'S VACCINE MANDATE
That's an important point because publicly, Australia's leaders are still pretending vaccination status matters. In New South Wales -- again, Eastern Australia -- one official promised that the unvaccinated will be allowed to retain their freedoms:DEPUTY PREMIER OF NEW SOUTH WALES JOHN BARILARO: The message to the unvaccinated is that you will not achieve any further freedom unless you get vaccinated and finally my message to south wales … There will be individuals in South Wales who choose not to be vaccinated who will lose their freedoms on the 11th of October.
No more freedom if you don’t get the vax, but, they will arrest you for being outside smoking a cigarette a block from your home without a mask, and not even ask you whether they’ve been vaccinated. So if vaccination status is that important as a health matter, wouldn’t that be the first question you ask? But they didn’t even bother. 
Meanwhile, in the same state -- New South Wales -- Australian officials are telling people that whether they're vaccinated or not, they can't go to church:
PASTOR: In the name of Jesus, lockdowns are over, in the cities of New South Wales. 
REPORTER: It’s unclear what passage this pastor is preaching from, but it’s not the public health order. His church the Christ Embassy in Blacktown is in lockdown, hard lockdown. … There was no QR code on the door. Costing the organization 5,000 dollars. Each of these thirty adult worshipers fined a thousand dollars. 
POLICE OFFICER: Whether it’s a soccer match, whether it’s a church service, it doesn’t matter. You cannot gather as they did at Blacktown.
Oh, so you have to get vaccinated to get any of your freedoms, but even if you are vaccinated, you’re not allowed to go to church. So what is the point of vaccination? Why did the federal government in Australia lock everyone down if there’s no actual way to stop the lockdowns. And more to the point, why do they want open borders in Western Australia if closing the borders has actually kept the population safe. 
COVID CASES SPIKE IN AUSTRALIAN STATE OF VICTORIA, GOVERNMENT BLAMES PEOPLE WATCHING SPORTS AT HOME
They want open borders there for the same reason they want them here. In New South Wales, one official -- the health officer -- made it explicit:
DR. KERRY CHANT: We will be looking at what contact tracing looks like in the new world order. Yes, it will be pubs and clubs and other things if we have a positive case there.
The new world order. She said it out loud. This is a really interesting story, what’s happening in Australia, and what it means for the rest of the Anglosphere, very much including us. And maybe that’s why globally, most media organizations have refused to cover it. That comment barely got any coverage at all. In fact, all the footage we just quoted is mostly being ignored in the United States. 
Why? It’s possible what’s happening in Australia might be instructive to us in the United States. In just two years, Australia's police went from raiding newsrooms to beating people in the street. Maybe the lesson is: Things can change very quickly. One moment, the English-speaking world is mocking China for being dystopian and autocratic. 
The next moment, they’re aping China and hunting people down who are two blocks from their home and smoking a cigarette. 
This article is adapted from Tucker Carlson's opening commentary on the Sept. 30, 2021 edition of "Tucker Carlson Tonight."
Get the recap of top opinion commentary and original content throughout the week.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
An unruly woman was captured on video ranting into a microphone about the COVID-19 pandemic during a commercial flight – much to the annoyance of her fellow passengers. 
The video was posted on TikTok by pop musician Jawny. 
"I bought in flight Wi-Fi just to post this," Jawny captioned the video. "We are in the air right now."
In the video, flight attendants struggle to contain the woman, who is seen wearing a white blouse and dark blue bottoms. 
"I brought my microphone, I’m going to use it," she says to a dismayed crew. "The pandemic started because humans have lost a little bit of faith." 
The flight attendants tell her that if she doesn’t go back to her seat, then they will be forced to cuff her. 
"You’re going to cuff me?" the woman asks repeatedly, sounding offended. "I’m completely harmless." 
LAGUARDIA ‘SECURITY INCIDENT’ PROMPTS PLANE EVACUATION
She then surmises that the passengers are enjoying the spectacle because "I’m not terrible to look at." 
She goes on to argue that the pandemic started because people are too glued to their electronic devices and can’t distinguish between the internet and reality. Passengers can be heard telling the woman she’s just looking for attention. 
"My dog has better sense than any of you," the woman says as flight attendants escort her to the back of the plane. "In fact, my dog could be a better God for you people." 
The video has received nearly 2 million views as of Monday evening. The woman's identity remains unknown. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Packers star receiver Davante Adams has been placed on the reserve/COVID-19 list, the team announced Monday.
The announcement comes as a huge blow to Green Bay (6-1), who are getting set for a heavyweight collision with the Cardinals (7-0) on Thursday night at 8:20 p.m. on FOX. Adams, 28, is arguably the best receiver in the NFL, racking up 744 yards on 52 receptions with three touchdowns this season.

      Green Bay Packers wide receiver Davante Adams (17) reacts during an NFL football game against the Cincinnati Bengals, Sunday, Oct. 10, 2021, in Cincinnati. Adams is on pace to accumulate more catches and yards receiving than he did last year while earning All-Pro honors.
      (AP Photo/Emilee Chinn)
With a short week ahead, the Packers have now moved into enhanced mitigation COVID protocols. That includes daily testing and required masking for all at the Packers facility, regardless of vaccination status. Adams doesn’t have much time to get off the list, meaning he will likely be out on Thursday night.

      Green Bay Packers wide receiver Davante Adams (17) catches a pass against Pittsburgh Steelers cornerback Joe Haden (23) in the third quarter at Lambeau Field.
      (Benny Sieu-USA TODAY Sports)
In his absence, quarterback Aaron Rodgers will lean on Allen Lazard, Randall Cobb and Robert Tonyan in the passing game. Running back Aaron Jones figures to see more opportunities as well, a role he’s accustomed to.

      Green Bay Packers quarterback Aaron Rodgers (12) hands the ball off to running back A.J. Dillon during the first half of an NFL football game Sunday, Oct. 17, 2021, in Chicago.
      (AP Photo/Nam Y. Huh)
AstraZeneca seeks U.S. approval for coronavirus drug. Fox News medical contributor Dr. Marc Siegel with insight on 'Fox & Friends.'
The U.S. is experiencing a decline in daily COVID-19 deaths after a two-month steady increase to mid-September, according to data compiled by the Centers for Disease Control and Prevention (CDC).
A seven-day moving average indicates a 12% decline over the last approximate two weeks, from 1,630 on Sept. 21 to 1,428 on Oct. 5, per the latest available figures. Nevertheless, the country logged a grim milestone late Friday when U.S. death toll from COVID-19 eclipsed 700,000.
US COVID-19 CASES, HOSPITALIZATIONS DOWN 30% OVER PRIOR MONTH
Also, as of Sept. 25, the death rate among adults ages 75 and older continued to exceed all other age groups at 2.09 per 100,000, whereas the rate for adults ages 65-74, 50-64 and 40-49 was 0.97, 0.44 and 0.23, respectively. The rate continued to decline and level off among younger populations ages 30-39 at 0.10 and a steady 0.02 among people ages 12-29, before hitting zero among kids under 11.
Americans over age 65 are tied with the highest uptake of at least one COVID-19 vaccine dose, at over 97% for adults ages 65-74, and about 92% for those 75 and older.
Dr. Rochelle Walensky, director of the CDC, noted the current "fairly constant" seven-day average of COVID-19 deaths, at around 1,400, at the Oct. 6 White House COVID-19 briefing. Walensky also warned of a potentially severe flu season this year, noting concern among experts of reduced population-level immunity against the seasonal flu owing to masking and distancing during the pandemic.
"An increase in flu infections and flu severity could put an additional burden on our health care system and increase stress on our nation’s healthcare workers," Walensky said, reiterating flu vaccination recommendations for everyone 6 months or older.
"Just like with COVID-19, we need as many people as possible to be vaccinated for influenza so that we can provide protection for those who are at most risk," including adults over 65, people with chronic health conditions and children, especially kids under age 5.
Walensky encouraged vaccinations against COVID-19 and the flu among eligible populations who have yet to receive shots. Federal figures indicate over 76% of Americans over age 12 have received at least one dose of COVID-19 vaccine, and about 66% are fully vaccinated. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
When Russian regulators approved the country's own coronavirus vaccine, it was a moment of national pride, and the Pavlov family was among those who rushed to take the injection. But international health authorities have not yet given their blessing to the Sputnik V shot.
So when the family from Rostov-on-Don wanted to visit the West, they looked for a vaccine that would allow them to travel freely — a quest that brought them to Serbia, where hundreds of Russian citizens have flocked in recent weeks to receive Western-approved COVID-19 shots.
Serbia, which is not a member of the European Union, is a convenient choice for vaccine-seeking Russians because they can enter the allied Balkan nation without visas and because it offers a wide choice of Western-made shots. Organized tours for Russians have soared, and they can be spotted in the capital, Belgrade, at hotels, restaurants, bars and vaccination clinics.

      People wait in line to receive a dose of a COVID-19 vaccine at Belgrade Fair makeshift vaccination center in Belgrade, Serbia, Saturday, Oct. 2, 2021. Russians are flocking to Serbia to receive Western-approved COVID-19 shots. Although Russia has its own vaccine known as Sputnik V, the shot has not been approved by international health authorities. (AP Photo/Darko Vojinovic)
      
"We took the Pfizer vaccine because we want to travel around the world," Nadezhda Pavlova, 54, said after receiving the vaccine last weekend at a sprawling Belgrade vaccination center.
Her husband, Vitaly Pavlov, 55, said he wanted "the whole world to be open to us rather than just a few countries."
Vaccination tour packages for Russians seeking shots endorsed by the World Health Organization appeared on the market in mid-September, according to Russia’s Association of Tour Operators.
Maya Lomidze, the group’s executive director, said prices start at $300 to $700, depending on what’s included.
Lauded by Russian President Vladimir Putin as world's first registered COVID-19 vaccine, Sputnik V emerged in August 2020 and has been approved in some 70 countries, including Serbia. But the WHO has said global approval is still under review after citing issues at a production plant a few months ago.

      Russian President Vladimir Putin speaks during a news conference after his meeting with U.S President Joe Biden at the 'Villa la Grange' in Geneva, Switzerland in Geneva, Switzerland, Wednesday, June 16, 2021. (AP Photo/Alexander Zemlianichenko, Pool)
      
On Friday, a top World Health Organization official said legal issues holding up the review of Sputnik V were "about to be sorted out," a step that could relaunch the process toward emergency use authorization.
FDA SAYS MODERNA VACCINE'S BENEFITS OUTWEIGH RISKS AFTER NORDIC COUNTRIES LIMIT USE
Other hurdles remain for the Russian application, including a lack of full scientific information and inspections of manufacturing sites, said Dr. Mariangela Simao, a WHO assistant director-general.
Apart from the WHO, Sputnik V is also still awaiting approval from the European Medicines Agency before all travel limitations can be lifted for people vaccinated with the Russian formula.
The long wait has frustrated many Russians, so when the WHO announced yet another delay in September, they started looking for solutions elsewhere.
"People don’t want to wait; people need to be able to get into Europe for various personal reasons," explained Anna Filatovskaya, Russky Express tour agency spokeswoman in Moscow. "Some have relatives. Some have business, some study, some work. Some simply want to go to Europe because they miss it."
Serbia, a fellow-Orthodox Christian and Slavic nation, offers the Pfizer, AstraZeneca and Chinese Sinopharm shots. By popular demand, Russian tourist agencies are now also offering tours to Croatia, where tourists can receive the one-shot Johnson & Johnson vaccine, without the need to return for a second dose.
DELTA COVID-19 VARIANT MORE DANGEROUS FOR UNVACCINATED PREGNANT WOMEN: STUDY
"For Serbia, the demand has been growing like an avalanche," Filatovskaya said. "It’s as if all our company is doing these days is selling tours for Serbia."
The Balkan nation introduced vaccination for foreigners in August, when the vaccination drive inside the country slowed after reaching around 50% of the adult population. Official Serbian government data shows that nearly 160,000 foreign citizens so far have been vaccinated in the country, but it is unclear how many are Russians.
In Russia, the country's vaccination rate has been low. By this week, almost 33% of Russia’s 146 million people have received at least one shot of a coronavirus vaccine, and 29% were fully vaccinated. Apart from Sputnik V and a one-dose version known as Sputnik Light, Russia has also used two other domestically designed vaccines that have not been internationally approved.
Russian Health Minister Mikhail Murashko recently said administrative issues were among the main holdups in the WHO’s review process.
Judy Twigg, a political science professor specializing in global health at Virginia Commonwealth University, expects Sputnik V to be approved eventually, but "maybe not by the end of this year."
"The WHO has said that it needs more data, and it needs to go back and inspect some production lines where it saw issues early on. Those re-inspections are a multiweek process, with good reason. It’s not something that they just gloss over lightly."
Amid low vaccination rates and reluctance by the authorities to reimpose restrictive measures, both Russia and Serbia have seen COVID-19 infections and hospitalizations reach record levels in the past weeks.
The daily coronavirus death toll in Russia topped 900 for a second straight day on Thursday — a day after reaching a record 929. In Serbia, the daily death toll of 50 people is the highest in months in the country of 7 million that so far has confirmed nearly 1 million cases of infection.
Pavlova said the "double protection" offered by the Pfizer booster shots would allow the family "to not only travel around the world, but also to see our loved ones without fear."
Since the vaccine tours exploded in popularity about a month ago, they have provided welcome business for Serbian tour operators devastated by the pandemic in an already weak economy. The owner of BTS Kompas travel agency in Belgrade, Predrag Tesic, said they are booked well in advance.
"It started modestly at first, but day by day numbers have grown nicely," Tesic said.
He explained that his agency organizes everything, from airport transport to accommodations and translation and other help at vaccination points. When they return for another dose in three weeks, the Russian guests also are offered brief tours to some of popular sites in Serbia.
Back in Russia, some Moscow residents said they understood why many of their fellow Russians travel abroad for vaccines. But Tatiana Novikova said homegrown vaccines remain her choice.
"I trust ours more, to be honest," she said.
Associated Press writers Dusan Stojanovic and Ivana Bzganovic in Belgrade, Serbia, and Daria Litvinova and Daniel Kozin reported from Moscow.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
What’s the latest advice on the type of mask I should wear?
CORONAVIRUS IN THE US: STATE-BY-STATE BREAKDOWN
It depends on your situation, but health officials say it should cover your nose and mouth, and fit snugly so there aren’t any gaps on the sides of your face.
The U.S. Centers for Disease Control and Prevention also says to pick masks with two or more layers and a nose wire to prevent air from leaking out the top. It suggests holding your mask up to check if it blocks light, which means the fabric will probably filter out more particles.
If you want added protection, experts also suggest wearing two masks or pairing them with a mask fitter to ensure they don’t leave any gaps.
FAUCI SAYS COVID-19 PANDEMIC UNCONTROLLED AS 66M REMAIN UNVACCINATED
It’s also important to find a mask that’s comfortable so you actually wear it, says Laura Kwong, an assistant professor in environmental health sciences at the University of California, Berkeley.
If supplies are available, people can opt for disposable N95 masks for personal use, the CDC says in updated guidance. Such masks are considered most effective at blocking virus particles. The agency had previously said N95 masks should be reserved for health care workers, but supplies have since expanded.
For people who are deaf or have hearing difficulties, alternative face coverings such as clear masks or cloth masks with clear plastic panels are recommended. Health officials say transparent medical masks should be prioritized for health workers and patients who need them.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
New York City public school teacher Nicole Broecker voices her frustration over unvaccinated teachers being placed on indefinite unpaid leave
New York City teachers and other school staff members are supposed to be vaccinated against COVID-19 when the bell rings Monday morning, in one of the first school district mandates in the country requiring employees to be inoculated against the coronavirus.
Mayor Bill de Blasio gave a final warning to the city's roughly 148,000 public school staffers on Friday, saying unvaccinated employees would be placed on unpaid leave and not be allowed to work this week. The city planned to bring in substitutes where needed.
Implementing the mandate smoothly may be a challenge for de Blasio, a Democrat who has boasted of the city’s record of keeping school buildings open during most of the last school year when other districts went to all-remote instruction. New York City is not offering a remote option this year.
ANTI-VACCINE0MANDATE PROTESTORS MARCH NYC STREETS ON EVE OF ENFORCEMENT FOR HEALTH CARE WORKERS

      Teachers protest against the COVID-19 vaccination mandates in New York on Wednesday Aug. 25, 2021. (AP Photo/Mary Altaffer, File)
      
De Blasio said 90% of Department of Education employees had received at least one vaccine dose, including 93% of teachers and 98% of principals, as of Friday.
The vaccination mandate in the nation’s largest school system does not include a test-out option but does allow for medical and religious exemptions. It was supposed to go into effect last week but was delayed when a federal appeals court granted a temporary injunction. An appeals panel reversed that decision three days later.
A similar mandate is set to go into effect in Los Angeles on Oct. 15.
Mark Cannizzaro, president of the Council of Schools Supervisors and Administrators, said that despite a surge in vaccinations last week, some principals can’t find enough staff to replace unvaccinated workers.
"While we’re thankful that the percentage of vaccinated staff has increased systemwide since the deadline was extended, there are still too many school leaders that have been unable to find qualified substitutes for Monday," Cannizzaro said.
A spokesperson for the United Federation of Teachers said the city "needs to work hard to make sure enough vaccinated personnel are in place to safely open the schools Monday morning."
Teachers and other school employees who had sued over the school vaccine mandate asked the U.S. Supreme Court on Thursday for an emergency injunction blocking its implementation. The request was denied on Friday.
Many students and parents support the vaccine mandate as the best way to keep schools open during the pandemic.

      Students are greeted by faculty as they arrive at PS811 in New York, Monday, Sept. 13, 2021.  (AP Photo/Richard Drew, File)
      
"It’s safer for our kids," said Joyce Ramirez, 28, who was picking her three children up from a Bronx elementary school last week.
Ramirez said she hopes the requirement will lessen the chances of teachers contracting the virus and prompting classroom or school shutdowns.
NYC MAYOR DE BLASIO GIVES FRIDAY DEADLINE FOR SCHOOL EMPLOYEES TO GET VACCINE AFTER LEGAL VICTORY
Cody Miller, a 15-year-old sophomore at a high school in Manhattan, said teachers should all be vaccinated. "I think they should," said the teen, who got vaccinated himself as soon as the Pfizer shot was approved for people 12 and up. "It’s so many kids, it’s a big environment, you know?"
But Mally Diroche, another Bronx parent, had mixed feelings. "I kind of feel like that’s a decision they should be able to make on their own," said the mom of three boys between 3 and 12. Diroche, 29, said she feels that masks and other precautions can check the virus’ spread within schools.
Some educators have reservations about the mandate but are complying.
Maurice Jones, 46, a support staff member at a Manhattan middle school, said he got vaccinated months ago but he sympathizes with co-workers who have not gotten the shots. "If they’ve got to get tested more they’ve got to get tested more," Jones said. "I don’t think they should lose their job."
Roxanne Rizzi, who teaches technology at an elementary school in Queens, waited until Friday to get her first coronavirus vaccine shot.
"I had to do it for the finances of my family," she said.
Rizzi, 55, had resisted the vaccine because she contracted COVID-19 in November and believed natural immunity would protect her. She said she would continue to protest the mandate.
According to the U.S. Centers for Disease Control and Prevention, people should get vaccinated even if they have already been infected by the virus. The agency says COVID-19 vaccines offer better protection than natural immunity and help prevent getting infected again.
Associated Press writer Jennifer Peltz contributed
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Justice is fully vaccinated, showed no symptoms
Supreme Court Justice Brett Kavanaugh tested positive for COVID-19, the court announced Friday, noting that he's fully vaccinated and showed no symptoms.
Kavanaugh learned of the positive test Thursday evening, ahead of Justice Amy Coney Barrett's ceremonial investiture Friday morning, according to a news release from the court.

      The Supreme Court announced Justice Brett Kavanaugh tested positive for the coronavirus on Thursday evening.
      
The release added that Kavanaugh's wife and daughters, all fully vaccinated, tested negative.
MARK LEVIN DISGUSTED BY POLITICIANS WHO 'HAVE POLITICIZED THE SCIENCE' OF COVID
"On Thursday, per the Court’s regular testing protocols, Justice Kavanaugh had a routine Covid test ahead of Justice Barrett’s investiture on Friday," the release said. "On Thursday evening, Justice Kavanaugh was informed that he had tested positive for Covid-19."
"He has no symptoms and has been fully vaccinated since January. Per current Court testing protocols, all of the Justices were tested Monday morning prior to conference, and all tested negative, including Justice Kavanaugh," it continued.
Barrett and Kavanaugh will be sitting at opposite ends of the table when oral arguments resume in the Supreme Court on Monday.
Kavanaugh ran in the Capital Challenge Road Race on Wednesday, with his team winning the three-mile race's judicial division with a 25 minute time.
Several lawmakers, judges and members of the media also participated in the race. Fox News' Sandra Smith placed first in the Electronic Journalist - Female category while Fox News took first in the Electronic Media category.
COVID-19 breakthrough cases have hit Capitol Hill recently. Fully vaccinated South Carolina Republicans Sen. Lindsey Graham and Rep. Ralph Norman tested positive for the virus in August.
As of Friday, the U.S. has 3.7 million COVID-19 cases and almost 52,000 deaths reported within the last 28 days, according to Johns Hopkins University's COVID-19 tracker.
Fox News' Shannon Bream and Bill Mears contributed to this report.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Durst was found guilty of killing a friend 20 years ago and was recorded saying 'I killed them all, of course' in 2015 documentary. Jacqui Heinrich reports.
Robert Durst, a convicted killer who tested positive for the coronavirus, is now on a ventilator, according to a report from Los Angeles' Fox 11.
In its report, an attorney for Durst confirmed the news that Durst was placed on a ventilator. 
ROBERT DURST GETS LIFE FOR CALIFORNIA MURDER OF BEST FRIEND
Durst, a 78-year-old New York real estate heir, was sentenced to life in prison in a Los Angeles County courtroom on Thursday for the 2000 murder of his longtime friend Susan Berman.
Durst was convicted last month of first-degree murder for shooting Berman in her Los Angeles-area home just before Christmas. Prosecutors alleged he killed her in an effort to silence her, as she was slated to talk to authorities about how she provided a phony alibi for Durst after his first wife vanished in 1982.
Kathie Durst went missing from the couple's South Salem, N.Y., home and has been declared dead, though her body has never been found. Durst has never been charged in her disappearance.
Several of the jurors who convicted Durst were present in the courtroom when the sentence was handed down. Durst declined to give a statement at his sentencing.
Fox News has reached out to Durst's attorneys.
Fox News' Louis Casiano contributed to this article.
Kyle Morris covers politics for Fox News and is a graduate of the University of Alabama. Follow him on Twitter: @RealKyleMorris
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
What is the "delta plus" variant? 
It’s a relative of the delta variant, identified by British scientists last month. 
Because it isn’t a variant of interest or concern, it has not yet been officially named after a letter of the Greek alphabet, like the other worrisome variants. 

      A person receives the Pfizer-BioNTech COVID-19 vaccine at a #VAXTOSCHOOL pop-up site at Life of Hope Center on Oct. 21 in New York City. 
      (Michael M. Santiago/Getty Images)
COVID-19 PANDEMIC: UP TO 180K HEALTH WORKERS MAY HAVE DIED, REPORT SAYS 
Scientists are monitoring the delta-related variant — known as AY.4.2. — to see if it might spread more easily or be more deadly than previous versions of the coronavirus. In a recent report, U.K. officials said this variant makes up 6% of all analyzed COVID-19 cases in the country and is "on an increasing trajectory." 
The variant has two mutations in the spike protein, which helps the coronavirus invade the body’s cells. These changes have also been seen in other versions of the virus since the pandemic started, but haven’t gone very far, said Francois Balloux, director of the Genetics Institute at University College London. 
The delta variant remains "by far the most dominant variant in terms of global circulation" said Maria Van Kerkhove, the World Health Organization’s technical lead on COVID-19, at a public session this week. 
"Delta is dominant, but delta is evolving," she said, adding that the more the virus circulates, the greater chances it has to mutate. 

      This photograph taken in March shows a sign of the World Health Organization  at the entrance of its headquarters in Geneva amid the COVID-19 outbreak.
      ( FABRICE COFFRINI/AFP via Getty Images)
The U.N. health agency is tracking 20 variations of the delta variant. The AY.4.2 is "one to watch because we have to continuously keep an eye on how this virus is changing," said Van Kerkhove. 
In the U.S., the delta variant accounts for nearly all COVID-19 cases. The newer "delta plus" variant has been spotted "on occasion," but it’s not yet a concern, health officials said. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
More than 2,000 tourists visiting China’s Inner Mongolia region have been sent to hotels to undergo two weeks of quarantine following the detection of new cases of COVID-19 in the area. 
The move follows reports of an outbreak of COVID-19 in the vast, lightly populated region that attracts visitors with its mountains, lakes and grasslands. 
An announcement from the regional government on Friday said 2,428 visitors had been placed under observation at hotels in the cities of Baotou and Ordos. 

      Service sector workers line up for a COVID-19 test during a mass testing at a site baring the words, "You and me on the road of civilization" in Beijing on Friday, following a spike of the coronavirus in the capital and other provinces. 
      (AP Photo/Andy Wong)
AUTHOR TELLS ‘AMERICAN STORY’ BEHIND COVID VACCINE DEVELOPMENT 
That came after successive reports of new cases of local infection in the region, with Inner Mongolia accounting for 19 of the 48 new cases of domestic transmission announced Friday. 
The quarantines are typical of the strict measures China has taken to control the pandemic, which also include mask wearing, electronic case tracing, mass testing, lockdowns and vaccinations. 

      In this aerial photo released by Xinhua News Agency, stranded self driving tourists prepare to leave Ejina Banner of Alxa League to head to quarantine hotels for two weeks, in northern China's Inner Mongolia Autonomous Region on Thursday.
      (Wang Xuebing/Xinhua via AP)
In the city of Lanzhou, in Gansu province bordering Inner Mongolia, millions of people have been largely confined to their homes over the past week after cases were detected there. Ten new cases were reported in the city on Friday. 

      A woman wearing a face mask to help curb the spread of the coronavirus walks through a line of masked service sector women waiting to receive a swab for the COVID-19 test during a mass testing in Beijing on Friday, following a spike of the coronavirus in the capital and other provincials. 
      (AP Photo/Andy Wong)
China has reported 4,636 deaths among 91,665 cases of COVID-19 recorded in the country since the first infections were detected in the central Chinese city of Wuhan in late 2019. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Anticipating a green light from vaccine advisers, the Biden administration is assembling and shipping millions of COVID-19 shots for children ages 5-11, the White House said Monday. The first could go into kids' arms by midweek. 
"We are not waiting on the operations and logistics," said coronavirus coordinator Jeff Zients. 
By vaccinating children, the U.S. hopes to head off another coronavirus wave during the cold-weather months when people spend more time indoors and respiratory illnesses can spread more easily. Cases have been declining for weeks, but the virus has repeatedly shown its ability to stage a comeback and more easily transmissible mutations are a persistent threat. 

      This October 2021 photo provided by Pfizer shows kid-size doses of its COVID-19 vaccine in Puurs, Belgium. 
      (Pfizer via AP, File)
NYC FIREFIGHTERS SUSPENDED, LOSE PAY AFTER ‘INAPPROPRIATE’ VACCINE PROTEST: ‘BLOOD ON THEIR HANDS’ 
On Tuesday, a special advisory panel to the Centers for Disease Control and Prevention will meet to consider detailed recommendations for administering the Pfizer-BioNTech vaccine to younger children. The Food and Drug Administration already cleared the shots, which deliver about one-third of the vaccine given to adults. After CDC advisers make their recommendations, agency director Dr. Rochelle Walensky will give the final order. 
Zients said the government has enough of the Pfizer vaccine for all 28 million children in the 5-11 age group. "We're in great shape on supply," Zients said during the White House coronavirus briefing. 
The children’s vaccination drive is expected to start later this week and go into full swing by next week. Parents will be able to go to vaccines.gov and filter on vaccines for children 5-11 to find a location near them that is offering the shot. 
Pfizer’s vaccine already has been authorized for use in older children. 
After the FDA gave its authorization for younger children, the Biden administration asked states, territories and other jurisdictions to place their initial orders. Workers at the drug company and at distribution centers began the process of preparing and packing 15 million doses, said Zients. 
"More doses will be packed and shipped and delivered," he added. "More and more vaccine will come on line as we ramp up." 

      A health worker in the U.K. prepares to administer a dose of Pfizer/BioNTech COVID-19 vaccine at a vaccination center. Soon, children in the United States may be able to receive the COVID-19 vaccine.
      (Dinendra Haria/SOPA Images/LightRocket via Getty Images)
The goal is for parents to have a range of options for getting children vaccinated, from pediatricians' offices to clinics and pharmacies. 
Walensky acknowledged both a sense of urgency and concern about getting children vaccinated. She stressed that clinical trials of the Pfizer vaccine for children have found it highly effective in preventing serious disease, with no severe adverse reactions in safety and efficacy trials. 
"There has been a great deal of anticipation from parents," Walensky said. "I encourage parents to ask questions." 
Separately, Zients announced that about 70% of U.S. adults are now fully vaccinated, while 80% have received at least one vaccine dose. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
U.S. Marine veteran Ronald Dean travels from California to Washington, D.C. to honor his fallen friends.
Tea party firebrand Allen West, a candidate for the Republican nomination for governor of Texas, said Saturday that he has received monoclonal antibody injections after being diagnosed with COVID-19 pneumonia.
The antibodies are used to treat those in the early stages of a coronavirus infection.
"My chest X-rays do show COVID pneumonia, not serious. I am probably going to be admitted to the hospital," West wrote. "There’s a concern about my oxygen saturation levels, which are at 89 and they should be at 95."
He also said his wife, Angela West, also tested positive and has received monoclonal antibodies. According to his Twitter account, Allen West did not get vaccinated against the virus, but his wife did.
REBA MCENTIRE REVEALS SHE CAUGHT CORONAVIRUS DESPITE BEING VACCINATED: ‘IT’S NOT FUN TO GET THIS'
Allen West on Thursday said he had attended a "packed house" Mission Generation Annual Gala & Fundraiser in Seabrook, Texas. On Saturday he tweeted that he is "suspending in-person events until receiving an all-clear indication."
West is a former Texas Republican Party chair and Florida congressman. He announced in July that he would challenge Republican Gov. Greg Abbot, who is running for a third term and has been endorsed by Donald Trump.
West's announcement came a month after he resigned as chair of the Republican Party of Texas.
West won a U.S. House seat in Florida in 2010 and quickly became a tea party favorite and lightning rod, at one point accusing Democrats of having as many as 80 communists in their House caucus. He failed to win reelection in 2012.
DEM STRATEGIST'S TWEET ABOUT LINDSEY GRAHAM'S COVID DIAGNOSIS PANNED
He later moved to Texas and largely stayed out of the spotlight until running for chairman of the state GOP party last year.
West then began criticizing Republicans as much as Democrats, calling the GOP speaker of the Texas House a "traitor" for working across the aisle, then leading a protest outside Abbott’s mansion over coronavirus restrictions.
In October 2020, West took part in a protest outside Abbot's home, criticizing the Republican governor's executive orders — including a statewide mask mandate and lockdowns due to the coronavirus pandemic. Those restrictions are no longer in place.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
F.L.A.G. CEO Nick Adams blasted the land Down Under over its 'extreme' policies regarding COVID-19.
Heavy marijuana users who are also vaccinated may be more susceptible to breakthrough cases of COVID-19, a new study found.
The study, published last Tuesday in World Psychology, found that those with a substance use disorder (SUD) — a dependence on marijuana, alcohol, cocaine, opioids and tobacco — were more likely to contract the coronavirus after receiving both of their vaccination shots.
Those without a SUD saw a 3.6 percent rate of breakthrough infections, compared to a 7 percent rate in those with a SUD. At 7.8 percent, those with marijuana use disorder were most at risk for breakthrough infections, the study found.
Among other substances, the risk disappeared when considering issues such as underlying health conditions and socioeconomic status. The difference has not been linked directly to marijuana use but could be linked to the behavior of those dependent on marijuana.
"Patients with cannabis use disorder, who were younger and had less comorbidities than the other SUD subtypes, had higher risk for breakthrough infection even after they were matched for adverse socioeconomic determinants of health and comorbid medical conditions with non-SUD patients," the researchers wrote.
"Additional variables, such as behavioral factors or adverse effects of cannabis on pulmonary and immune function, could contribute to the higher risk for breakthrough infection in this group."
Marijuana advocates said the study did not show that marijuana could be a cause in breakthrough cases, also noting that most marijuana users are not dependent on the drug.
"This study is limited to people with ‘substance use disorder’ which is a very small subset of cannabis consumers," Morgan Fox, media relations director for the National Cannabis Industry  Association told Newsweek. 
"This is merely correlation and does not show a causal relationship … individual behavior patterns and social conditions may be a major contributing factor above and beyond simply exhibiting problematic substance use patterns, such as lack of access to reliable information, sharing joints, etc," she said.
"Clearly more study is welcome and necessary, but it is important not to overstate or misrepresent the very inconclusive results presented in this particular research and ensure that cannabis consumers are accurately informed about what the newest research actually indicates," Fox added.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
WAUKESHA, Wis. (AP) – A parent has sued a southeastern Wisconsin school district after her son contracted COVID-19 from a classmate.
The Milwaukee Journal Sentinel reported that Shannon Jensen filed the lawsuit in federal court against the Waukesha School District and school board on Oct. 5. Jensen is seeking an injunction ordering the district to comply with U.S. Centers for Disease Control COVID-19 guidelines.
MSNBC's CHRIS HAYES HIT FOR SPREADING ‘MISINFORMATION’ ABOUT MONOCLONAL ANTIBODY TREATMENTS
According to the lawsuit, the board in May removed a student mask requirement and other COVID-19 mitigation measures. 
One of Jensen’s son’s classmates came to school with symptoms in September and didn’t wear a mask. Jensen’s son was seated next to the sick student and was wearing a mask but still became infected. Jensen’s other two sons later tested positive as well.
SMOKING MARIJUANA COULD LEAD TO BREAKTHROUGH COVID CASES, STUDY FINDS
School Board President Joseph Como declined comment on the lawsuit.
The Minocqua Brewing Company Super PAC is funding the lawsuit. 
The brewing company is owned by Kirk Bangstad, who has aired his frustrations about how former President Trump’s administration responded to the pandemic. He ran unsuccessfully against incumbent Republican state Rep. Rob Swearingen last year.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
CEO of Scotland County Hospital Dr. Randy Tobler joins 'Fox & Friends First' to tell why he believes there will be a labor shortage due to vaccine mandates, says people will chose freedom instead
With the U.S. averaging nearly 90,000 new COVID-19 infections each day and some 66 million Americans remaining unvaccinated, Dr. Anthony Fauci, President Biden’s chief medical adviser, said the country needs to gain control to approach normalcy. 
"Much of the world, and in some respects including ourselves, are still in the pandemic phase," Fauci told a virtual White House briefing Wednesday, later adding, "We’re looking for a level of control of the virus that would allow us to be able to essentially approach the kind of normal that we are all craving for and that we all talk about."

      Dr. Anthony Fauci, President Biden’s chief medical adviser, said the country needs to gain control over the COVID-19 pandemic to approach normalcy. 
      
While the U.S. is experiencing a decline across new infections, hospitalizations and deaths, Fauci said a threshold for adequate control would involve fewer than 10,000 daily new cases.
"It is going to be very difficult, at least in the foreseeable future and maybe ever, to truly eliminate this highly transmissible virus," Fauci told the briefing, pointing to surges in case numbers during the spring, summer and fall of 2020, and most recently, late summer of 2021. He noted that while each time reported cases accelerated and later diminished, the country never gained proper control.
"We can get to control without a doubt, it is within our power and within our capability," Fauci said, citing a fivefold reduction in risk of infection among fully vaccinated individuals compared to those yet to receive shots, as well as an over tenfold drop in hospitalization and death risk, respectively. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Australian journalist harassed by police talks to Laura Ingraham 
Thousands of demonstrators marched down Rome’s Via Veneto and other main streets on Saturday, some clashing with police, to protest a government rule requiring COVID-19 vaccines or negative tests to access workplaces next week.
THOUSANDS PROTEST WASHINGTON STATE'S VACCINE MANDATE, SING NATIONAL ANTHEM
The certification in Italy, known as a "Green Pass," takes effect on Friday and applies to public and private workplaces.

      People gather in Piazza del Popolo square during a protest, in Rome, Saturday, Oct. 9, 2021. Thousands of demonstrators protested Saturday in Rome against the COVID-19 health pass that Italian workers, both the public and private sectors, must display to access their workplaces from Oct. 15 under a government decree. 
      (Cecilia Fabiano/LaPresse via AP)
To obtain one, people must either have had at least one COVID-19 vaccine dose, document recovery from the illness in the last six months or test negative in the previous 48 hours.

      A doll with syringes is shown by a demonstrator during a protest, in Rome, Saturday, Oct. 9, 2021. Thousands of demonstrators protested Saturday in Rome against the COVID-19 health pass that Italian workers, both the public and private sectors, must display to access their workplaces from Oct. 15 under a government decree. 
      (Cecilia Fabiano/LaPresse via AP)
VATICAN TO MANDATE VACCINES FOR EMPLOYEES 
Both employees and employers risk fines if they don’t comply. Workers in the public sector can be suspended if they show up five times without a Green Pass. This summer, Green Passes were required in Italy to enter museums, theaters, gyms and indoor restaurants, and take long-distance trains and buses or domestic flights.
The protesters held an authorized protest in Piazza Del Popolo. Then some left the vast square and clashed with police as they went to an unauthorized march. Police in helmets and carrying shields and batons blocked them from marching down a street that runs past Premier Mario Draghi’s office.

      Police clashes with demonstrators during a protest, in Rome, Saturday, Oct. 9, 2021. Thousands of demonstrators protested Saturday in Rome against the COVID-19 health pass that Italian workers, both the public and private sectors, must display to access their workplaces from Oct. 15 under a government decree.
      (Cecilia Fabiano/LaPresse via AP)
As of Saturday, 80% of those 12 and older have been fully vaccinated in Italy.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News correspondent Rich Edson reports on China's timeline for the development of the coronavirus on 'Special Report'
This is a rush transcript of "Special Report" on October 7, 2021. This copy may not be in its final form and may be updated.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The COVID-19 patient's health was deteriorating quickly at a Michigan hospital, but he was having none of the doctor's diagnosis. Despite dangerously low oxygen levels, the unvaccinated man didn't think he was that sick and got so irate over a hospital policy forbidding his wife from being at his bedside that he threatened to walk out of the building.
Dr. Matthew Trunsky didn’t hold back in his response: "You are welcome to leave, but you will be dead before you get to your car,’" he said.
Such exchanges have become all-too-common for medical workers who are growing weary of COVID-19 denial and misinformation that have made it exasperating to treat unvaccinated patients during the delta-driven surge.
The Associated Press asked six doctors from across the country to describe the types of misinformation and denial they see on a daily basis and how they respond to it.
They describe being aggravated at the constant requests to be prescribed the veterinary parasite drug Ivermectin, with patients lashing out at doctors when they are told that it's not a safe coronavirus treatment. An Illinois family practice doctor has patients tell him that microchips are embedded in vaccines as part of a ploy to take over people's DNA. A Louisiana doctor has resorted to showing patients a list of ingredients in Twinkies, reminding those who are skeptical about the makeup of vaccines that everyday products have lots of safe additives that no one really understands.
Here are [some of] their stories:
When patients tell Dr. Vincent Shaw that they don’t want the COVID-19 vaccine because they don’t know what’s going into their bodies, he pulls up the ingredient list for a Twinkie.

      Sept. 29, 2021: Dr. Vincent Shaw poses for a portrait in Baton Rouge, La. He commonly hears patients tell him they haven't done enough research on the COVID-19 vaccines. Rest assured, he tells them, the vaccine developers have done their homework. 
      (AP Photo/Dorthy Ray)
"Look at the back of the package," Shaw, a family physician in Baton Rouge, Louisiana. "Tell me you can pronounce everything on the back of that package. Because I have a chemistry degree, I still don’t know what that is."
He also commonly hears patients tell him they haven’t done enough research about the vaccines. Rest assured, he tells them, the vaccine developers have done their homework.
Then there are the fringe explanations: "They’re putting a tracker in and it makes me magnetic."
Another explanation left him speechless: "The patient couldn’t understand why they were given this for free, because humanity in and of itself is not nice and people aren’t nice and nobody would give anything away. So there’s no such thing as inherent good nature of man. And I had no comeback from that."
People who get sick with mild cases insist that they have natural immunity. "No, you’re not a Superman or Superwoman," he tells them.
He said one of the biggest issues is social media, as evidenced by the many patients who describe what they saw on Facebook in deciding against getting vaccinated. That mindset has spawned memes about the many Americans who got their degrees at the University of Facebook School of Medicine.
"I am like, ‘No, no, no, no, no.’ I shake my head, ‘No, no. That is not right, no, no. Stop, stop, just stop looking at Facebook.’"
Dr. Stu Coffman has patients tell him they are scared about vaccine side effects. They don’t trust the regulatory approval process and raise disproven concerns that the vaccine will harm their fertility. He said the most unexpected thing someone told him was that there was "actually poison in the mRNA vaccine" — a baseless rumor that originated online.
He is confounded by the pushback.
GET THE FOX NEWS APP
"If you’ve got a gunshot wound or stab wound or you’re having a heart attack, you want to see me in the emergency department," he said. "But as soon as we start talking about a vaccine, all of a sudden I’ve lost all credibility."
He said the key to overcoming hesitancy is to figure out where it originates. He said when people come to him with concerns about fertility, he can point to specific research showing that the vaccine is safe and their issues are unfounded.
But he says there's no hope in changing the minds of people who think the vaccines are laced with poison. "I’m probably not going to be able to show you anything that convinces you otherwise."
And he thinks he could change people’s minds about the vaccine if they could follow him around for a shift as he walks past the beds of the sick and dying, almost all of whom are unvaccinated.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
ESPN college football sideline reporter Allison Williams said Friday night she is leaving the company over a coronavirus vaccine mandate issued for all Disney employees.
Williams said last month she was advised by her doctor to forgo getting the coronavirus vaccine because she was trying to get pregnant. She said the decision to skip the vaccine sidelined her from working college football games. She said in an Instagram video on Friday her "request for accommodation" was denied.

      ESPN Sideline Reporter Allison Williams interviews Head Coach Manny Diaz of the Miami Hurricanes after the game against the Florida State Seminoles at Doak Campbell Stadium on Bobby Bowden Field on November 2, 2019 in Tallahassee, Florida. Miami defeated Florida State 27 to 10.
      (Photo by Don Juan Moore/Getty Images)
Essentially, Williams said it came down to a moral dilemma for her.
"Belief is a word I’ve been thinking about a lot lately, because in addition to the medical apprehensions regarding my desire to have another child in regards to receiving this injection, I am also so morally and ethically not aligned with this. And I’ve had to really dig deep and analyze my values and my morals, and ultimately I need to put them first," she said, via Awful Announcing.
"And the irony in all this is that a lot of these same values and morals that I hold dear are what made me a really good employee, what helped with the success that I’m able to have in my career."
Additionally, Williams said she wasn’t going to "put a paycheck over principle."
COVID-19 VACCINATION AMONG PREGNANT WOMEN REMAINS LOW DESPITE SEVERE RISK

      ESPN side line reporter Allison Williams walks on the field during the College Football Playoff Semifinal at the Rose Bowl football game between the Alabama Crimson Tide and the Notre Dame Fighting Irish at AT&amp;T Stadium on January 01, 2021 in Arlington, Texas.
      (Photo by Alika Jenner/Getty Images)
"I don’t know what the future holds, obviously, for any of us. I’m trying to wrap my head around the thought that the largest game I’ve worked in my career, the national championship game, might be the last game I work. But I’m going to focus on what I have to be thankful for," she said. 
"I’m going to hold on to my faith. I’m going to pray that things get better, and that I can see you on the television set in some capacity, in some stadium, covering some game soon. Until then, God bless, and I’m going to go hug my baby."
Vaccination against COVID-19 is recommended for all people 12 years and older, including people who are pregnant, breastfeeding, trying to get pregnant now, or might become pregnant in the future.
The CDC wrote late last month to urge increased COVID-19 vaccination among people who are pregnant, recently pregnant, who are trying to become pregnant or who might become pregnant in the future.
"The CDC health advisory strongly recommends COVID-19 vaccination either before or during pregnancy because the benefits of vaccination for both pregnant persons and their fetus or infant outweigh known or potential risks. Additionally, the advisory calls on health departments and clinicians to educate pregnant people on the benefits of vaccination and the safety of recommended vaccines," the CDC said, noting that vaccination rates vary markedly by race and ethnicity with coverage highest among Asian people who are pregnant.
DO COVID-19 VACCINES AFFECT MY CHANCES OF PREGNANCY?
Williams made the announcement she was not working college football games this season last month.
"While my work is incredibly important to me, the most important role I have is as a mother. Throughout our family planning with our doctor, as well as a fertility specialist, I have decided not to receive the COVID-19 vaccine at this time while my husband and I try for a second child," she said in a statement.

      Dec 26, 2019; Detroit, Michigan, USA; Pittsburgh Panthers wide receiver Maurice Ffrench (2) smiles with Allison Williams after the game against the Eastern Michigan Eagles at Ford Field.
      (Raj Mehta-USA TODAY Sports)
"This was a deeply difficult decision to make and it’s not something I take lightly. I understand vaccines have been essential to the effort to end this pandemic; however, taking the vaccine at this time is not in my best interest. After a lot of prayer and deliberation, I have decided I must put my family and personal health first. I will miss being on the sidelines and am thankful for the support of my ESPN family. I look forward to when I can return to the games and job that I love."
Disney, which is the parent company of ESPN, said in August it would be requiring the vaccine and the mandate includes those who work for the sports entertainment company outlet, according to the Bristol Press.
Williams joined ESPN in March 2011. She previously worked for Fox Sports Florida covering the Florida Marlins and Florida Panthers.
Fox News’ Julia Musto contributed to this report.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The NFL is encouraged by the progress made in preventing any major spreads of COVID-19 among the 32 teams, while concerned about an increase in soft tissue injuries.
Dr. Allen Sills, the league's chief medical officer, noted Tuesday at the first in-person owners meetings since December 2019 that a low positive COVID-19 rate between .04% and .06% is due greatly to vaccinations and protocols working. Nearly 100,000 COVID-19 tests have been taken, 1,200 a day on average across the league.
So far, 94.1% of players are vaccinated, as well as 100% of team and league staff.
"We're continuing to work with the players association on the goal of 100% vaccination," Sills said. "The CDC has been in contact with us about how that is achieved, a vaccination success story, and is pointing to the NFL as a model for other parts of society."
Sills mentioned a recent mini-outbreak with the Arizona Cardinals that included coach Kliff Kingsbury.
"Of the first seven cases in Arizona, five were different strains of the virus," he said, which indicated those people were exposed outside the team facility. "Definitely the impact of vaccinations, we're not seeing the clustering or uncontrolled spread of the virus. Nor are we seeing the uncontained, unexplainable, uncontrolled spread we saw last year."
The league is undertaking a voluntary study of antibody levels to measure and compare who was vaccinated when and which medication, and whether the person had COVID-19. Sills called it a "unique study because of size and the frequent testing." Players can participate but are not the focus, club employees are.
As for the soft tissue injuries (hamstring, groin, calf, et al), the numbers are up to a five-year high even though the overall amount of preseason injuries went down. Of course, there were only three preseason games for 30 of the teams during the summer.
Sills cited the amount of work required of players in a short timeframe, and expressed a need for significant load management to combat the problem.
"There's a lot to unpack there and we will have more to say about this, I think, as we approach the combine (in late winter)," he said. "This year (such injuries) were particularly noteworthy."
The 2022 combine will be in Indianapolis, but the 2023 event will be put up for bidding, with Dallas, Los Angeles and Indianapolis interested.
Members of the NFL’s Social Justice Working Group and the owners of all 32 teams were given a copy of a letter by two former employees of the Washington Football Team asking them to make public a report on the league’s 10-month investigation into the franchise.
The employees allege the team engaged in harassment and abuse for decades.
NFL spokesman Jeff Miller would not comment on the letter, saying Commissioner Roger Goodell later would speak on it — if he wanted to address the topic.
"I love for this to be a learning point, not just for the NFL, but for leagues and teams all across that this shouldn’t be hidden," said Ana Nunez, who worked in the team’s business department until 2019. "There shouldn’t be, no workplace is perfect which is understandable, but there has to be a level of accountability when it comes to toxic culture and sexual harassment."
Melanie Coburn, a Washington cheerleader for four years, then marketing coordinator and director until 2011, said she wants to see the report from outside counsel Beth Wilkinson, who conducted the NFL investigation, and not a watered-down version from the league.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Italian city that suffered the brunt of COVID-19’s first deadly wave is dedicating a vivid memorial to the pandemic dead: A grove of trees, creating oxygen in a park opposite the hospital where so many died, unable to breathe.
Bergamo, in northern Italy, is among the many communities around the globe dedicating memorials to commemorate lives lost in a pandemic that is nearing the terrible threshold of 5 million confirmed dead.
Some have been drawn from artists’ ideas or civic group proposals, but others are spontaneous displays of grief and frustration. Everywhere, the task of creating collective memorials is fraught, with the pandemic far from vanquished and new dead still being mourned.
Memorial flags, hearts, ribbons: These simple objects have stood in for virus victims, representing lost lives in eye-catching memorials from London to Washington D.C., and Brazil to South Africa.
The collective impact of white flags covering 20 acres on the National Mall in the U.S. capital was literally breathtaking, representing the more than 740,000 Americans killed by COVID-19, the highest official national death toll in the world.
FLORIDA COVID CASES, DEATH RATE AMONG LOWEST IN THE COUNTRY
One honored 80-year-old Carey Alexander Washington of South Carolina, who was vaccinated and contracted the virus while still working as a clinical psychologist in March. His 6-year-old granddaughter Izzy collapsed in grief when she found her ‘’papa’s" flag -- a moment captured by a photographer and shared on Twitter.

      Zoe Nassimoff, of Argentina, looks at white flags that are part of artist Suzanne Brennan Firstenberg's temporary art installation, "In America: Remember," in remembrance of Americans who have died of COVID-19, on the National Mall in Washington, Sept. 17, 2021.
      (Associated Press)
"Families like mine, we’re still grieving," said Washington's daughter, Tanya, who traveled from Atlanta to see the memorial. "It was important to witness that honor that was being given to them. It gave a voice to all our loved ones that have been lost."
A memorial wall in London similarly conveys the scale of loss, with pink and red hearts painted by bereaved loved ones on a wall along the River Thames. Walking the memorial’s length without pausing to read names and inscriptions takes a full nine minutes. The hearts represent the over 140,000 coronavirus deaths in Britain, Europe’s second-highest toll after Russia; like elsewhere in the world, the actual number is estimated to be much higher:160,000.
"It shocks people,’’ said Fran Hall, a spokeswoman for the COVID-19 Bereaved Families for Justice. She lost her husband, Steve Mead, in September 2020, the day before his 66th birthday. "Every time we are here, people stop and talk to us, and quite often they are moved to tears as they are walking by, and thank us."

      Erika de Vasconcelos Machado, 40, places her hand on her father's name inscribed on the In-Finito Memorial, installed to comfort family members and honor those who died from COVID-19, at the Penitence Crematorium and Cemetery, in the Caju neighborhood of Rio de Janeiro, Brazil, Wednesday, Oct. 27, 2021. 
      (Associated Press)
In Brazil’s capital, relatives of COVID-19 victims planted thousands of white flags in front of Brazil’s Congress in a one-day, emotion-laden action meant to raise awareness of Brazil’s toll of more than 600,000, the second-highest in the world.
And in South Africa, blue and white ribbons are tied to a fence at the St. James Presbyterian Church in Bedford Gardens, east of Johannesburg, to remember the country’s 89,000 dead: each blue ribbon counting for 10 lives, white for one.
How victims of war, atrocities and even health crises are remembered has evolved through the ages. Victorious statues of generals gave way to tombs of the unknown soldier after World War I, in a bid to remember the sacrifices of ordinary soldiers. Paris’ Arche de Triomphe was one of the first.
"World War I was a benchmark, which is particularly relevant because it was followed by the 1918 flu pandemic," said Jennifer Allen, an assistant professor of history at Yale University who has studied memorial culture.
That pandemic seems to have been little memorialized, partly because of the keen focus on the war dead. "It was a period of mass death," Allen said. "That is why we talk about the lost generation."
Holocaust memorials were the next major testaments to mass killing, Allen said. They span big, traditional monuments like Berlin’s Holocaust Memorial, and more personalized tributes where victims are named, like the so-called Stumbling Stones outside buildings were Jews lived before the Holocaust.

      Volunteers work on the COVID-19 memorial wall in Westminster in London, Friday, Oct. 15, 2021. 
      (Associated Press)
Not since the AIDS quilt made its way across the United States, with loved ones adding squares for people who had succumbed, has a health crisis been the object of memorials of a scale like those now honoring the COVID-19 dead. The quilt has grown to nearly 50,000 squares, representing more than 105,000 individuals.
Memorials like the AIDS quilt and the Stumbling Stones have helped solidify a trend toward grass-roots remembrances and the desire to honor victims as individuals, Allen said. Both are emerging in the COVID-19 memorials.
"We want to get to the individuals, who make up all of the millions of deaths,’’ Allen said. "As people so often point out: These were mothers, fathers, brothers, sisters, children, neighbors. "
Collectively memorializing the coronavirus dead has been complicated by the weight of private grief, which was too often borne alone in the first wave, when funerals could not take place and loved ones too often died without the presence or caress of a loved one.
An Italian Facebook group, Noi Denunceremo, was started as a place to publicly, if virtually, remember the dead during the country’s first draconian lockdown, and developed quickly into a collection of data on alleged failures that have been turned over to prosecutors.
In India, one of the world's most affected countries, an online memorial was launched in February, www.nationalcovidmemorial.in, inviting submissions verified with death certificates. So far, it has only 250 tributes, a minute fraction of the over 457,000 confirmed dead, which is itself a vast undercount.
"It’s not memorializing only, it’s how we can pay respect and dignity" to the dead, said Abhijit Chowdhury of the COVID Care Network that started the memorial from the eastern city of Kolkata.
In Russia’s second-largest city, St. Petersburg, a bronze statue called "Sad Angel" was placed in March outside a medical school to honor the dozens of doctors and medical workers who died of COVID-19. The sculpture of an angel with his shoulders slumped and head hanging disconsolately is especially poignant because its creator, Roman Shustrov, himself died of the virus in May 2020.
Italy has not dedicated a national monument to its some 132,000 confirmed dead, but it has designated a coronavirus remembrance day. Premier Mario Draghi stood among the first newly planted trees in Bergamo’s Trucca Park on March 18, the first anniversary of the indelible image of army trucks bringing dead to other cities for cremation after the city’s morgue was overwhelmed.
Bergamo’s mayor said the city considered proposals for statues or plaques bearing the names of the dead. One was too monumental; the other ignored that so many dead were not officially counted due to lack of testing.
"The Woods of Memory is a living monument, and it immediately seemed to us to be the most convincing, the most emotive and the one that was closest to our sentiments,’’ Bergamo Mayor Giorgio Gori said.
Only 100 trees have been planted so far of the 700 that are planned, facing the hospital’s morgue. The rest should be planted by next year's March 18 remembrance day.
There are no plans to add names, but in at least one case, loved ones have claimed a sapling: Roses are planted at the base, with personal mementoes hanging from it and a white rock bearing the handwritten name of a dearly departed: Sergio.
AP journalists Pan Pylas in London, Phil Marcelo in Boston, Sheikh Saaliq in New Delhi, Mogomotsi Magome in Johannesburg, Irina Titova in St. Petersburg, Russia, and Débora Álvares in Brasilia, Brazil, contributed to this report.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The U.S. Food and Drug Administration (FDA) is expected to allow the mixing and matching of COVID-19 vaccine booster doses this week, according to reports.
The forthcoming announcement by the agency is anticipated as the campaign for additional shots continues and as more Americans head back for a third jab. 
SAN FRANCISCO SHUTS DOWN IN-N-OUT FOR NOT ENFORCING JAB MANDATE: 'WE REFUSE TO BECOME THE VACCINATION POLICE'
The Associated Press reported on Tuesday – citing an anonymous U.S. health official familiar with the matter – that the news would likely be put out alongside the authorization for boosters of the Moderna and Johnson & Johnson shots, though the FDA was still predicted to say that using the same brand for a booster was the preferable option and especially for mRNA vaccines from Pfizer and Moderna.
The FDA declined to comment.
Last month, regulators OK'd a third dose for the Pfizer/BioNTech vaccine for many Americans and last week the U.S. said it would recognize combinations of vaccines administered overseas for the purpose of entering the country.

      In this March 3, 2021 file photo, a vial of the Johnson &amp; Johnson COVID-19 vaccine is displayed at South Shore University Hospital in Bay Shore, N.Y.
      (AP Photo/Mark Lennihan, File)
While receiving a different COVID-19 vaccine booster from the one initially received could simplify the booster process – in addition to allowing those with adverse reactions to the initial dose to try a different shot – questions remain.
Moderna has applied for its booster to be half of the original dose, but a National Institutes of Health study of booster combinations used full-strength extra doses. 
FDA PANEL ENDORSES JOHNSON & JOHNSON COVID-19 VACCINE BOOSTER WITH 2-MONTH GAP FOR AGES 18 AND UP
Preliminary results found that an extra dose of any type increases the amount of virus-fighting antibodies, with recipients of the single-dose Johnson & Johnson vaccination showing the most remarkable response. 
The New York Times reported Tuesday that vaccine providers could also use their discretion to offer a different brand.
The newspaper said that the FDA was projected to authorize the Moderna and Johnson & Johnson boosters by Wednesday night and that a U.S. Centers for Disease Control and Prevention (CDC) advisory committee would take up the topic on Thursday before issuing its own recommendations. 
The Times said that officials are expected to authorize a booster of Moderna's vaccine about six months after the second shot and a Johnson & Johnson booster would be allowed at least two months after the first dose.
They also pointed out that the mix and match study's researchers warned against using findings to conclude that any single combination of vaccines was better than the others.
All of this comes after lengthy deliberation about the need for boosters shots at all, as vaccines in the U.S. remain effective against hospitalization and death from the virus and its delta variant.
More than 189 million Americans are fully vaccinated, according to CDC data.
The Associated Press contributed to this report
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
As the nation rebounds from a surge of the delta variant, questions swirl over future and new coronavirus variants and the effectiveness of vaccines against them.
As long as the virus that caused the COVID-19 pandemic continues to infect people, new variants will continue to emerge. 
FRONT-LINE HEALTH CARE WORKER SHORTAGE DUE TO COVID-19 VACCINE MANDATES, BURNOUT
However, that does not mean that variants will occur with the same frequency or become more hazardous.
Last week, the U.K. Health Security Agency said that a delta descendant called AY.4.2 was "expanding" and "increasing in frequency" in England. 
In a statement to Business Insider, the U.S. Centers for Disease Control (CDC) said Wednesday that the variant is still very rare, at "well below 0.05%" of all sequenced viruses, with less than 10 reported in the agency's database thus far. 

      A woman wearing a mask passes by a coronavirus disease mobile testing van in Washington Square Park in New York City, U.S., July 22, 2021.
      (REUTERS/Brendan McDermid/File Photo)
"At this time … there is no evidence that the sub-lineage A.Y.4.2 impacts the effectiveness of our current vaccines or therapeutics," the CDC said.
Andrew Read, a virus expert at Pennsylvania State University, told The Associated Press that a virus needs to adapt to its host to spread more widely and the CDC says that the delta variant is doubly as contagious as earlier versions of the virus. 
However, while the virus could become more infectious, there is no evolutionary reason for it to become more deadly.
"We’ve seen a stage of rapid evolution for the virus. It’s been harvesting the low-hanging fruit, but there’s not an infinite number of things it can do," Dr. Adam Lauring, a virus and infectious disease expert at the University of Michigan, told the AP.
FLORIDA'S NEW SURGEON GENERAL: DATA DOES NOT SUPPORT MASK MANDATES IN SCHOOL
Those who are severely ill are also less likely to socialize and spread the virus to others. 
With more than half of the world still unvaccinated, the virus is likely to continue to infect, replicate and potentially mutate – creating new variants. 
Nearly 190 million people, or about 57% of the total population, are fully vaccinated in the U.S.
Scientists are monitoring whether new variants could better evade the protection afforded to people through vaccination and infection, making the immune responses less effective.
If that happens, experts may promote periodically updated vaccine formulas, as in the case of annual flu shots.
Pfizer, Inc. CEO Albert Bourla said in June that, should the need arise, his company could develop a new COVID-19 vaccine within 100 days. 
Nature reported on Wednesday that the makers of the Pfizer/BioNTech, Moderna and AstraZeneca vaccines have been "running dress rehearsals" and practicing on known variants in clinical studies.
Moderna, the publication said, is recruiting hundreds of participants to test new RNA vaccines against the beta and delta variants, a combination of beta and the original strain and a beta-delta multivalent vaccine.
The Associated Press contributed to this report
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Braves right fielder Jorge Soler was pulled from the lineup for Tuesday's Game 4 of the NL Division Series against Milwaukee after testing positive for COVID-19.
Outfielder Cristian Pache took Soler’s spot on the roster, Major League Baseball announced.
Soler was replaced at the top of the order by shortstop Dansby Swanson. Joc Pederson, slated to start in left field, shifted to right. Guillermo Heredia was inserted in center field batting eighth, and Adam Duvall switched from center to left.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Eagles tight end Dallas Goedert may miss Thursday night’s game against the Buccaneers.

      Dallas Goedert #88 of the Philadelphia Eagles looks on against the Kansas City Chiefs at Lincoln Financial Field on Oct. 3, 2021 in Philadelphia, Pennsylvania. 
      (Tim Nwachukwu/Getty Images)
On Tuesday, Philadelphia announced that its starting tight end was placed on the Reserve/COVID-19 list. Goedert is the second Eagles player on the list, along with guard Sua Opeta.
TOM BRADY PLANS TO PLAY DESPITE HEAVILY WRAPPED RIGHT HAND

      Dallas Goedert #88 of the Philadelphia Eagles drops a pass during the second half against the Carolina Panthers at Bank of America Stadium on Oct. 10, 2021 in Charlotte, North Carolina. 
      (Mike Comer/Getty Images)
Goedert was listed on Monday’s injury report with an illness.
If Goedert does indeed miss the team’s game against Tom Brady and the Bucs, Eagles quarterback Jalen Hurts will be without one of his favorite targets through the first five games of the NFL season.

      Dallas Goedert #88 of the Philadelphia Eagles leaps over Daniel Sorensen #49 of the Kansas City Chiefs at Lincoln Financial Field on Oct. 3, 2021 in Philadelphia, Pennsylvania. 
      (Tim Nwachukwu/Getty Images)
Goedert has 15 receptions for 216 yards and two touchdowns. He ranks sixth among all NFL tight ends in yards after the catch (813) and tied for eighth in receiving touchdowns (14) since he was drafted in the second round of the 2018 NFL Draft.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The World Health Organization (WHO) announced 26 proposed members to an advisory committee aimed to steer studies into the origin of the COVID-19 pandemic and other pathogens of epidemic potential.
The Scientific Advisory Group for the Origins of Novel Pathogens (SAGO) marks the global health agency’s latest attempt to unravel the beginnings of the coronavirus pandemic nine months after sending experts to China. In March, the WHO had released its report on the origins of the coronavirus, with the research team listing introduction through an intermediary host followed by zoonotic transmission as "likely to very likely" the root of initial spread, and introduction through a laboratory incident as "extremely unlikely."
COACHELLA WILL NO LONGER REQUIRE COVID VACCINE FOR ENTRY
Overall, without a definitive conclusion as to how the virus made its way into the human population, the team, which comprised of international experts, had called for "a continued scientific and collaborative approach to be taken towards tracing the origins of COVID-19."  
"The emergence of new viruses with the potential to spark epidemics and pandemics is a fact of nature, and while SARS-CoV-2 is the latest such virus, it will not be the last," Dr Tedros Adhanom Ghebreyesus, WHO director-general, said in a statement issued Wednesday. "Understanding where new pathogens come from is essential for preventing future outbreaks with epidemic and pandemic potential, and requires a broad range of expertise."
The WHO noted the dozens of proposed members were selected from a pool of over 700 applications. The 26 members have expertise in fields such as "epidemiology, animal health, ecology, clinical medicine, virology, genomics," among others.
"We are very pleased with the calibre of experts selected for SAGO from around the world, and look forward to working with them to make the world safer," Tedros said.
There will be a two-week public consultation period for the WHO to receive feedback on the proposed SAGO members and set in place modalities for its first meeting following the consultation period.
CORONAVIRUS IN THE US: STATE-BY-STATE BREAKDOWN
In its capacity as an advisory body to WHO, the SAGO will advise the organization on the development of a WHO global framework to define and guide studies into the origins of emerging and re-emerging pathogens of epidemic and pandemic potential, as well as advise the WHO on prioritizing studies and field investigations into the subjects.
In addition, the committee will provide information and opinions to assist the WHO Secretariat in the development of a detailed work plan of the SAGO. 
In the context of the origins of the SARS-CoV-2 virus, the SAGO will provide the WHO Secretariat with an independent evaluation of all available scientific and technical findings from global studies and advise the WHO Secretariat regarding developing, monitoring and supporting the next series of related studies, the release reads. 
The SAGO will provide "rapid advice" on the WHO's operational plans to implement the next series of global studies into the origins of SARS-CoV-2, outlined in a March report. Last, the committee will provide any additional advice and support to the WHO, as requested by the WHO SAGO Secretariat, including participation in future WHO-international missions to study the origins of SARS-CoV-2 or other emerging pathogens.
Reuters reported that the WHO launched the request for applications last August and September.
A public list of the proposed members provided by the WHO shows that the original team of 10 international experts are listed on the committee, including Dutch virologist Marion Koopmans, Danish epidemiologist Thea Fischer, British epidemiologist John Watson, Russian researcher Vladimir Dedkov, animal health specialist Hung Nguyen of Vietnam and epidemiologist Elmoubasher Farag of Qatar.
Any future investigations in China could potentially prove difficult as the country has repeatedly said it considers investigation of COVID-19′s origins there completed.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Gabby Reichardt says the school is allowing alumni, donors and parents to come and go without providing vaccine information while students are required to comply
The U.S. Navy announced Thursday that it is preparing to discharge sailors who refuse vaccination for COVID-19 as mandated by the Pentagon, and the service members who get the boot over their noncompliance run the risk of losing some veterans benefits.
The Navy sent out a press release noting that Nov. 14 is the deadline for active-duty sailors to get either their second shot of a two-dose vaccine or the single shot of a one-dose vaccine. Reservists have until Dec. 14.

      WASHINGTON, DC - SEPTEMBER 17: Members of the Navy Ceremonial Guard stand for the national anthem during a ceremony for National POW/MIA Recognition Day, at the U.S. Navy Memorial on September 17, 2021 in Washington, DC. The ceremony honored all military personnel who were prisoners of war or who are still missing in action. (Photo by Kevin Dietsch/Getty Images)
      (Kevin Dietsch)
ARMY OFFICER RESIGNS OVER BIDEN VACCINE MANDATE, ‘MARXIST TAKEOVER OF THE MILITARY’
Sailors who do not have a pending or approved exemption by the deadlines set will face administrative actions and "those separated only for vaccine refusal will receive no lower than a general discharge under honorable conditions" the Navy's statement read, adding, "This type of discharge could result in the loss of some veterans’ benefits."
The Navy said it "may also seek recoupment of applicable bonuses, special and incentive pays, and the cost of training and education for service members refusing the vaccine."

      WASHINGTON, DC - SEPTEMBER 17: A member of the Navy Ceremonial Guard stands for the national anthem during a ceremony for National POW/MIA Recognition Day, at the U.S. Navy Memorial on September 17, 2021 in Washington, DC. The ceremony honored all military personnel who were prisoners of war or who are still missing in action. (Photo by Kevin Dietsch/Getty Images)
      (Kevin Dietsch)
RON JOHNSON PENS LETTER TO BIDEN, DOD QUESTIONING MILITARY VACCINE MANDATES
"Sailors must be prepared to execute their mission at all times, in places throughout the world, including where vaccination rates are low and disease transmission is high," the Navy stated. "Immunizations are of paramount importance to protecting the health of the force and the warfighting readiness of the Fleet."
The Navy says 98% of its active duty members are already vaccinated against the coronavirus.

      INDIANAPOLIS, IN - SEPTEMBER 12: US Navy service members are seen before the Indianapolis Colts and Seattle Seahawks game at Lucas Oil Stadium on September 12, 2021 in Indianapolis, Indiana. (Photo by Michael Hickey/Getty Images)
      (Michael Hickey)
The Department of Defense announced in late August that all members of the armed forces must get vaccinated against COVID-19, just days after the Food and Drug Administration granted full approval for the Pfizer-BioNTech vaccine.
President Joe Biden has mandated that all federal employees be fully vaccinated by Nov. 22, and that all federal contractors have a fully vaccinated workforce by Dec. 8. He has also directed OSHA to issue a forthcoming regulation ordering all U.S. businesses with more than 100 employees to require their workers to either get vaccinated or submit to weekly coronavirus tests.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
New York City officially declared racism a public health crisis in the city. 
"We must confront racism as a public health crisis. This pandemic magnified inequities, leading to suffering disproportionately borne by communities of color. But these inequities are not inevitable," New York City Health Commissioner Dave Chokshi wrote on Twitter Monday.
The city’s Board of Health passed a resolution on Monday that cited America’s history with slavery and the impacts of the coronavirus felt by minority communities. The Board of Health is mostly composed of members appointed by Democratic Mayor Bill de Blasio, the New York Post reported. 
CHICAGO MAYOR DECLARES RACISM A PUBLIC HEALTH CRISIS
The resolution calls on health officials to help address racism in their own policies, including implementing policies for "a racially just recovery from COVID-19, as well as other actions to address this public health crisis in the short and long term." 
Other actions include: establishing ​​"a Data for Equity internal working group to ensure the agency apply an intersectional, anti-racism equity lens to public health data and provide annual guidance to other NYC Mayoral agencies on best practices to collect and make available to the Health Department relevant data to track and improve health equity;" and "That the NYC Health Department make recommendations on anti-racism, health-related NYC Charter revisions to the newly established Mayoral Racial Justice Commission to strengthen the NYC’s effort to combat racism."
"We have chosen our words carefully this afternoon in presenting this to you as a resolution—rather than just a declaration—because we must be resolute," Chokshi said at the board meeting, according to the Gothamist. "We must resolve to take action beyond our recognition of the problem."
Other cities have also declared racism a public health crisis in recent months.
Chicago Mayor Lori Lightfoot declared racism a public health emergency in June. The city’s public health department said it would also allocate nearly $10 million in coronavirus relief funds to establish six Healthy Chicago Equity Zones to help improve community living. 
"At almost every single point in our city's history, racism has taken a devastating toll on the health and well-being of our residents of color – especially those who are Black," Lightfoot said in a statement. "Without formally acknowledging this detrimental impact, we will never be able to move forward as a city and fully provide our communities with the resources they need to live happy and healthy lives."
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The U.S. Food and Drug Administration (FDA) announced Monday that it had issued an emergency use authorization for the ACON Laboratories Flowflex COVID-19 Home Test.
The over-the-counter (OTC) COVID-19 antigen test will be added to the growing list of tests that can be used at home without a prescription. 
CDC RENEWS RECOMMENDATION FOR VIRTUAL HOLIDAY CELEBRATIONS
The agency said that the authorization is expected to double rapid at-home testing capacity over the next several weeks and that by the end of the year, ACON expects to produce more than 100 million tests per month and potentially 200 million tests per month by February 2022.
"This action highlights our continued commitment to increasing the availability of appropriately accurate and reliable OTC tests to meet public health needs and increase access to testing for consumers," Jeffrey E. Shuren, director of FDA’s Center for Devices and Radiological Health, said in a statement.
Since March 2020, the FDA has reportedly authorized more than 400 COVID-19 tests and sample collection devices.
Most of the antigen tests for at-home use are authorized for serial testing or testing the same person more than once within a few days. 
Based on data for asymptomatic individuals, the ACON Laboratories Flowflex COVID-19 Home Test does not require serial testing.
These authorizations, the FDA noted, come on the heels of a previous commitment to streamline the path for COVID-19 screening tools, providing a supplemental template for test developers seeking emergency use authorization of certain tests for screening with serial testing and issuing a fact sheet that outlines considerations for selecting a test for use in a screening testing program. 
COVID-19: 90% OF POPULATION MAY NEED TO BE VACCINATED TO END PANDEMIC
In its release, the FDA reminded patients and users that all tests can experience false-negative and false-positive results.
The agency also stressed the importance of at-home diagnostic testing in the fight against the coronavirus.
"We believe at-home diagnostic tests play a critical role in the fight against COVID-19. We will continue to offer support and expertise to help with the development of appropriately accurate and reliable tests, and to facilitate increased access to tests for all Americans," Shuren wrote.
San Diego-based ACON Laboratories Inc. said in its own accompanying statement that the nasal swab test would soon be available for purchase in major retail stores and online and would be used by individuals 14 years and older, or with adult-collected nasal swabs from children as young as 2 years old.
"In contrast to other home tests which require testing twice within a two-to-three-day period (a process known as serial screening), the Flowflex COVID-19 Antigen Home Test has been authorized for use as a single test by individuals with or without symptoms. This will allow for the distribution of more affordable single-test packaging, resulting in greater access to home testing," ACON Laboratories said.
President Biden highlighted rapid tests in a speech in December, pledging that the government would purchase 280 million tests and that it would use the Defense Production Act to ensure manufacturers have the raw materials they need to make tests.
The administration is spending approximately $2 billion on the initiative.
The Associated Press contributed to this report.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Children's Hospital Colorado declares a mental health state of emergency; Fox News correspondent Aishah Hasnie reports on the startling statistics.
More than 140,000 U.S. children lost a parent, grandparent or other caregiver to COVID-19, a study found, with researchers noting significant racial and ethnic disparities and calling for a focused effort to protect kids’ mental health and well-being.
The federally funded findings, published in the Pediatrics journal, resulted from a collaboration between Centers for Disease Control and Prevention researchers and several universities, and included data from April 1, 2020, to June 30, 2021, finding that about 1 in 500 U.S. kids have been affected by COVID-associated orphanhood.
The loss of a parent or grandparent who provides care and basic needs can increase children’s risk of poor mental health and self-esteem and give way to substance abuse, suicide, violence and sexual abuse, according to the National Institutes of Health (NIH).
EARLY ADULTHOOD DEPRESSION INCREASES DEMENTIA RISK, STUDY FINDS

      Saturday, Oct. 2, 2021: A visitor sits on a bench to look artist Suzanne Brennan Firstenberg's "In America: Remember," a temporary art installation made up of white flags to commemorate Americans who have died of COVID-19, on the National Mall, in Washington.
      (AP Photo/Jose Luis Magana)
"Children facing orphanhood as a result of COVID is a hidden, global pandemic that has sadly not spared the United States," said Susan Hillis, CDC researcher and lead author of the study, in an NIH news release posted Thursday. "All of us – especially our children – will feel the serious immediate and long-term impact of this problem for generations to come."
Hillis stressed that addressing children's losses should be one of the top priorities amid the pandemic and post-pandemic response.
The team of researchers conducted the study by analyzing mortality, fertility and census data across the U.S. and for each state, with COVID-19-associated deaths referring to both direct and indirect causes, like COVID-19 disease or lockdowns, reduced quality of health care and disease treatment. Results indicated about 120,630 U.S. children lost a parent or grandparent who provided basic needs and care, whereas another 22,007 kids lost a secondary caregiver, or grandparents offering housing but not basic needs, per the release.
"The death of a parental figure is an enormous loss that can reshape a child’s life," said Dr. Nora Volkow, director of the National Institute on Drug Abuse. "We must work to ensure that all children have access to evidence-based prevention interventions that can help them navigate this trauma, to support their future mental health and wellbeing."
"At the same time, we must address the many underlying inequities and health disparities that put people of color at greater risk of getting COVID-19 and dying from COVID-19, which puts children of color at a greater risk of losing a parent or caregiver and related adverse effects on their development," Volkow added.
Researchers found significant disparities; while White individuals comprise 61% of the population and minorities make up 39% of the population, White children accounted for 35% of those who lost a primary caregiver, whereas kids of racial and ethnic minorities comprised 65% of those who lost a caregiver.
Compared to White children, American Indian/Alaska Native children were 4.5 times more likely to lose a parent or grandparent caregiver. Black children were associated with a 2.4-times greater likelihood of losing a parent or grandparent when compared with White children, while Hispanic children faced a 1.8-times greater likelihood, the release reads. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Rep. Glenn Thompson, R-Pa., has tested positive for the coronavirus and is currently receiving treatment at a hospital, according to a statement shared from his staff.
CDC MASK GUIDELINES UNDER REVIEW AS COVID NUMBERS FALL, COLD SEASON BEGINS
Congressman Thompson on Friday afternoon began experiencing cold-like symptoms and was promptly tested for COVID-19," reads the statement, which was shared to Twitter. "While he is vaccinated, the test case back positive."

      Glenn Thompson (R-PA) is sworn in by Speaker of the House Nancy Pelosi during a mock ceremony on Capitol Hill, January 6, 2008, in Washington, D.C. (Photo by Andrew Councill/MCT/Tribune News Service via Getty Images)
      
The staff also noted that "out of an abundance of caution," Thompson is receiving treatment at Walter Reed National Military Medical Center in Bethesda, Maryland.

      BETHESDA, MD - OCTOBER 04: A general view of the facade of Walter Reed National Military Medical Center. (Photo by Samuel Corum/Getty Images)
      
"He is in good spirits and further updates will be made available in the coming days," the statement concluded.
Kyle Morris covers politics for Fox News and is a graduate of the University of Alabama. Follow him on Twitter: @RealKyleMorris
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
'Fox Across America' host Jimmy Failla with reaction on 'Fox & Friends First.'
Florida has seen a dramatic reversal of fortune this week with some of the lowest COVID numbers in the country, marking a dramatic change from this summer when it ranked among the worst. 
As of Wednesday, the Sunshine State was averaging 60.6 cases and 0.2 deaths per 100,000 people, according to the Centers for Disease Control and Prevention (CDC). 

      Florida Gov. Ron DeSantis speaks at a news conference, Thursday, Sept. 16, 2021, at the Broward Health Medical Center in Fort Lauderdale, Fla. 
      (AP Photo/Wilfredo Lee, file)
"As Florida now ranks lowest in the continental U.S. in terms of COVID-19 rates per capita, we are proud to have stood firm in protecting liberty throughout the pandemic," Lt. Gov. Jeanette Nunez said in a statement. "Governor DeSantis' approach was guided by science, data and pragmatism, not fear and alarmist narratives." 
In August, when the delta variant was spreading throughout the country, Florida had among the highest new cases in the nation — a seven-day moving average of more than 21,000, according to the CDC. That figure has steadily dropped ever since. 

      People wait in cars to get a COVID-19 test, Wednesday, Aug. 11, 2021, in Miami. 
      (AP)
Critics blamed the high cases and deaths on Republican Gov. Ron DeSantis’s policies, arguing that he was not being proactive enough. 
DeSantis Press Secretary Christina Pushaw said when COVID cases were high, she was inundated with media requests. But now that case and death rates are low, coverage has conspicuously fizzled out. 
DESANTIS: WE ARE ACTIVELY RECRUITING OUT-OF-STATE POLICE OFFICERS OUT OF JOB DUE TO VACCINE MANDATES
"They were writing non-stop negative stories about COVID in Florida and implying that it was the governor’s fault," Pushaw told Fox News. "But now that we have the lowest infection rate in the entire country, those same media outlets are silent. So, you would think, if it was his fault at the peak, why isn’t his credit right now?
"It just shows they’re using this for their own political ends, their own ends, they’re not even being consistent with it," Pushaw said. 
DeSantis’ approach contrasted sharply with the likes of California’s Gov. Gavin Newsom, who shut down large swaths of the state and imposed strict mask mandates – despite having roughly similar outcomes as Florida. 

      President Biden, right, looks at Florida Gov. Ron DeSantis, left, during a briefing with first responders and local officials in Miami, Thursday, July 1, 2021, on the condo tower that collapsed in Surfside, Fla.
      (AP)
DeSantis has resisted sweeping mandates, having vowed legal action over federal vaccination requirements and having fought masking and vaccine rules implemented by local governments in Florida. 
"The fact is, policies – whether they're lockdowns, mask mandates, vaccine mandates – those do not actually make a difference in terms of COVID prevalence. But what a governor can make a difference in is protecting individual rights," Pushaw said. 
At a press conference Thursday, DeSantis announced that the state of Florida is suing the Biden administration over its coronavirus mandate for federal contractors, saying the president does not have the authority to issue the rule and that it violates procurement law. 
The Associated Press contributed to this report. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
New York Congresswoman Elise Stefanik says Republicans will stand up for American's freedoms against forced vaccines.
The United States Army has launched an investigation into reports that three people were accidentally given the coronavirus vaccine at a Washington state military base.
"Joint Base Lewis-McChord is aware three people were inadvertently administered the Pfizer COVID-19 vaccine instead of another vaccine at the Lewis Main Exchange," Lt. Col. Joey Sollinger with I Corps Public Affairs told the Military Times.

      FILE - In this March 3, 2021 file photo, a vial of the Johnson &amp; Johnson COVID-19 vaccine is displayed at South Shore University Hospital in Bay Shore, N.Y. (AP Photo/Mark Lennihan, File)
      
COVID-19 SIDE EFFECTS COULD INCLUDE MEMORY LOSS, BRAIN FOG, RESEARCHERS FIND
Sollinger added that "positive corrective action has been taken at this vaccination site to prevent such errors from happening again" adding that an investigation has been launched.
The accidental vaccinations occurred at Joint Base Lewis-McChord south of Tacoma, Washington. The base is home to I Corps and 62d Airlift Wing.
BLACKBURN BILL WOULD EXEMPT ESSENTIAL WORKERS FROM FIRING FOR DEFYING COVID VACCINE MANDATES

      Los Angeles, CA - May 13: Bottles of the three current COVID-19 vaccines from Johnson &amp;amp; Johnson, Moderna and Pfizer, with hypodermics needles, photographed at the COVID-19 vaccination site at Kedren Community Health Center, in Los Angeles, CA, Thursday, May 13, 2021.
      (Jay L. Clendenin / Los Angeles Times via Getty Images)

      View of the Pfizer Global Research and Development Laboratories on Friday, August 21, 2009 in San Diego, CA.Many pharmaceutical companies are in a race to find cancer killing drugs. (Photo by Sandy Huffaker/Corbis via Getty Images)
      (Photo by Sandy Huffaker/Corbis via Getty Images)
The military has not confirmed the identities of the people involved.
As of Oct. 21, the Defense Department has reported 248,865 cases of COVID-19 across the services, with 1,282 new reports between Oct. 13 and Oct. 20.
Andrew Mark Miller is a writer at Fox News. Follow him on Twitter @andymarkmiller and email tips to AndrewMark.Miller@Fox.com
 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The global death toll from COVID-19 topped 5 million on Monday, less than two years into a crisis that has not only devastated poor countries but also humbled wealthy ones with first-rate health care systems. 
Together, the United States, the European Union, Britain and Brazil — all upper-middle- or high-income countries — account for one-eighth of the world’s population but nearly half of all reported deaths. The U.S. alone has recorded over 740,000 lives lost, more than any other nation. 
"This is a defining moment in our lifetime," said Dr. Albert Ko, an infectious disease specialist at the Yale School of Public Health. "What do we have to do to protect ourselves so we don’t get to another 5 million?" 

      Reena Kesarwani holds a photograph of her husband, Anand Babu Kesarwani, who died of COVID-19, in their hardware shop, Oct. 25, 2021, in the Chhitpalgarh village in India's northern Uttar Pradesh state. 
      (AP Photo/Rajesh Kumar Singh)
NEW YORK CITY FIREFIGHTERS TAKE MEDICAL LEAVE AMID LOOMING VACCINE SANCTIONS 
The death toll, as tallied by Johns Hopkins University, is about equal to the populations of Los Angeles and San Francisco combined. It rivals the number of people killed in battles among nations since 1950, according to estimates from the Peace Research Institute Oslo. Globally, COVID-19 is now the third-leading cause of death, after heart disease and stroke. 
The staggering figure is almost certainly an undercount because of limited testing and people dying at home without medical attention, especially in poor parts of the world, such as India. 
Hot spots have shifted over the 22 months since the outbreak began, turning different places on the world map red. Now, the virus is pummeling Russia, Ukraine and other parts of Eastern Europe, especially where rumors, misinformation and distrust in government have hobbled vaccination efforts. In Ukraine, only 17% of the adult population is fully vaccinated; in Armenia, only 7%. 
"What’s uniquely different about this pandemic is it hit hardest the high-resource countries," said Dr. Wafaa El-Sadr, director of ICAP, a global health center at Columbia University. "That’s the irony of COVID-19." 
Wealthier nations with longer life expectancies have larger proportions of older people, cancer survivors and nursing home residents, all of whom are especially vulnerable to COVID-19, El-Sadr noted. Poorer countries tend to have larger shares of children, teens and young adults, who are less likely to fall seriously ill from the coronavirus. 
India, despite its terrifying delta surge that peaked in early May, now has a much lower reported daily death rate than wealthier Russia, the U.S. or Britain, though there is uncertainty around its figures. 
The seeming disconnect between wealth and health is a paradox that disease experts will be pondering for years. But the pattern that is seen on the grand scale, when nations are compared, is different when examined at closer range. Within each wealthy country, when deaths and infections are mapped, poorer neighborhoods are hit hardest. 
In the U.S., for example, COVID-19 has taken an outsize toll on Black and Hispanic people, who are more likely than White people to live in poverty and have less access to health care. 
"When we get out our microscopes, we see that within countries, the most vulnerable have suffered most," Ko said. 
Wealth has also played a role in the global vaccination drive, with rich countries accused of locking up supplies. The U.S. and others are already dispensing booster shots at a time when millions across Africa haven’t received a single dose, though the rich countries are also shipping hundreds of millions of shots to the rest of the world. 
Africa remains the world’s least vaccinated region, with just 5% of the population of 1.3 billion people fully covered. 
In Kampala, Uganda, Cissy Kagaba lost her 62-year-old mother on Christmas Day and her 76-year-old father days later. 

      A medical worker prepares a shot of Russia's Sputnik Lite coronavirus vaccine at a vaccination center in the GUM, State Department store, in Red Square with the St. Basil Cathedral in the background in Moscow, Russia, on Oct. 26, 2021. 
      (AP Photo/Pavel Golovkin, File)
"Christmas will never be the same for me," said Kagaba, an anti-corruption activist in the East African country that has been through multiple lockdowns against the virus and where a curfew remains in place. 
The pandemic has united the globe in grief and pushed survivors to the breaking point. 
"Who else is there now? The responsibility is on me. COVID has changed my life," said 32-year-old Reena Kesarwani, a mother of two boys, who was left to manage her late husband’s modest hardware store in a village in India. 
Her husband, Anand Babu Kesarwani, died at 38 during India's crushing coronavirus surge earlier this year. It overwhelmed one of the most chronically underfunded public health systems in the world and killed tens of thousands as hospitals ran out of oxygen and medicine. 
In Bergamo, Italy, once the site of the West’s first deadly wave, 51-year-old Fabrizio Fidanza was deprived of a final farewell as his 86-year-old father lay dying in the hospital. He is still trying to come to terms with the loss more than a year later. 
"For the last month, I never saw him,’’ Fidanza said during a visit to his father's grave. "It was the worst moment. But coming here every week, helps me." 
Today, 92% of Bergamo’s eligible population have had at least one shot, the highest vaccination rate in Italy. The chief of medicine at Pope John XXIII Hospital, Dr. Stefano Fagiuoli, said he believes that’s a clear result of the city’s collective trauma, when the wail of ambulances was constant. 
In Lake City, Florida, LaTasha Graham, 38, still gets mail almost daily for her 17-year-old daughter, Jo’Keria, who died of COVID-19 in August, days before starting her senior year of high school. The teen, who was buried in her cap and gown, wanted to be a trauma surgeon. 
"I know that she would have made it. I know that she would have been where she wanted to go," her mother said. 

      A woman walks through a line of masked service sector women waiting to receive a swab for a COVID-19 test during a mass testing in Beijing on Oct. 29, 2021, following a spike of the coronavirus in the capital and other provincials. 
      (AP Photo/Andy Wong, File)
In Rio de Janeiro, Erika Machado scanned the list of names engraved on a long, undulating sculpture of oxidized steel that stands in Penitencia cemetery as an homage to some of Brazil’s COVID-19 victims. Then she found him: Wagner Machado, her father. 
"My dad was the love of my life, my best friend," said Machado, 40, a saleswoman who traveled from Sao Paulo to see her father’s name. "He was everything to me." 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Lingering COVID-19 symptoms in "long haulers" may be caused by an overload of inflammatory cells "trapped" inside insoluble microscopic blood clots, according to researchers at Stellenbosch University in South Africa.  
Professor Resia Pretorius, a member of the university’s Physiological Sciences Department, made the finding with her research team while studying micro clots in blood samples of individuals with "long COVID." 
"We found high levels of various inflammatory molecules trapped in micro clots present in the blood of individuals with long COVID," Pretorius stated in a news release. "Some of the trapped molecules contain clotting proteins such as fibrinogen, as well as alpha (2)-antiplasmin". 

      A study found "long COVID" symptoms may be caused by trapped inflammatory cells in micro blood clots.
      (iStock, File)
FRANCIS COLLINS, LONGTIME HEAD OF NIH, TO RESIGN 
Fibrinogen is a protein involved with clot formation, while the molecule, Alpha (2)-antiplasmin, prevents the breakdown of blood clots, the authors explained in the release.  
Typically, the body is able to maintain a balance between the process of blood clotting (thickening of the blood to prevent blood loss after an injury) and fibrinolysis (the breakdown of fibrin in blood to prevent blood clot formation), according to health experts. 
However, when high levels of alpha (2)-antiplasmin are present in the blood of patients infected with COVID-19 and those dealing with "long COVID," the body’s ability to break down the clots is significantly hampered, the researchers explained in the study. 
The researchers also noted a significant discovery, that the samples of blood plasma collected from acute COVID-19 and "long COVID" patients continued to deposit insoluble pellets at the bottom of the tubes of samples.
The research team was the first to report finding these micro clots in blood samples of COVID patients, helping solve another puzzling component of the disease, according to the study.  
"Of particular interest is the simultaneous presence of persistent anomalous micro clots and a pathological fibrinolytic system," the authors stated in their report.  
The research teams said these findings provide further evidence that COVID-19 and "long COVID" had significant cardiovascular and clotting pathologies. They recommended further research into treatment therapies to support the clotting and fibrinolytic system in patients with "long COVID" symptoms.  
Study shows Merck's anti-viral pill cuts hospitalization and death by 50%
Mount Sinai South Nassau Chief of Infectious Disease Dr. Aaron Glatt, a spokesman for the Infectious Diseases Society of America, was not involved in the study, but told Fox News: "This is an interesting but very preliminary finding that must be investigated further before any clinical actions can be taken based upon this data." 
The hospital epidemiologist added, "We currently do not have a complete understanding of ‘long COVID’ by any means, but hopefully this will be another piece in the puzzle that will allow us to better understand and treat this important and common complication of COVID-19 illness." 
The study was peer-reviewed and published in the journal Cardiovascular Diabetology  in August 2021.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News' Janice calls for continued investigations into New York's handling of COVID-19 deaths and says she'd like to see all states under a federal probe.
"Apologies aren’t meant to change the past, they are meant to change the future." 
I remembered that quote on Tuesday on my way home with my husband Sean after meeting New York Gov. Kathy Hochul. We were invited to the meeting after the governor saw us at a rally outside her Manhattan office a few weeks ago when we were advocating on behalf of the loved ones we lost to COVID last spring in separate long term care facilities. 
It was a small, closed door meeting. There were no pictures taken inside the office.  It was simply a moment to finally speak and be heard.

       Daniel Arbeeny, Haydee Pabney, Assemblyman Ron Kim, Alexa Rivera Janice Dean, her husband Sean Newman and Peter Arbeeny pose for a photo before meeting with New York Gov. Hochul  about 2020 COVID nursing home deaths on October 12, 2021.
      
COVID-19 NURSING HOME DEATHS IN 2020 MUCH HIGHER THAN PREVIOUSLY THOUGHT: STUDY
This was the first time our family has ever been acknowledged by the governor’s office. As she walked in and shook our hands, she offered her condolences.
 "I’m sorry for your loss."
I thanked her for taking the time to sit with us, and find out what we’ve been fighting for all these months.
Without any of us knowing on March 25th of 2020 former Gov. Andrew Cuomo issued an executive order to admit over 9,000 COVID positive patients into New York nursing homes for 46 days.  Even Cuomo knew this would endanger our seniors when he pre-emptively warned the virus would "spread like fire through dry grass." 
NEW NY GOV. KATHY HOCHUL ADDS 12,000 DEATHS TO COVID DEATH COUNT
It’s still a mystery to us as to why he and his health office decided to light the match.
Instead of being honest, and admitting this was a terrible decision, Cuomo lied, denied, blamed others while covering up the death toll.  While he could’ve met with families or expressed his condolences, the governor decided it was more important to celebrate himself by writing a book and winning an Emmy.
As grieving family members, many of us wanted some kind of acknowledgement for our pain and grief.  Instead, we were accused of playing politics for wanting to know why our loved ones were put in grave danger. 
My good friend and fellow advocate New York State Assemblyman Ron Kim, who lost his uncle to COVID in a nursing home help arrange the sit down. 
JANICE DEAN: MY IN-LAWS DIED FROM COVID IN 2020. THIS WEEK WE WERE ABLE TO PUBLICLY CELEBRATE THEIR LIVES
I am so grateful for his kindness and leadership through all of this.  Tuesday’s meeting would never have happened without him. 
Gov. Hochul was empathetic and generous with her time.  She wanted to hear from all of us, and listened to our thoughts and concerns about how we can finally start the healing process and the way forward to help make sure it doesn’t happen again.
My husband Sean, who is a very private person, finds it very difficult to talk about his loss. He was able explain to her how painful it was losing both his parents in such a short period of time without being able to see or comfort them. 

      Dee and Mickey Newman in an undated family photograph.
      (Courtesy Janice Dean)
He told her how he brought his mom flowers a few days after his father died, but couldn’t hug her. He stood six feet away in the lobby of her assisted living residence telling her to hang on. We’d get through this. 
That was the last time he saw her before she got sick and died. 

      Janice Dean's in-laws Dee and Mickey Newman attend their son Sean's promotion ceremony to battalion chief
      (Courtesy Janice Dean)
Seeing my husband sharing this with the governor brought me right back to what it was like a year and a half ago. The shock, confusion, and grief crashed over me so hard I could barely catch my breath.
I cried listening to my friends Peter and Daniel Arbeeny talk about their father Norman, asking if his death counted in Gov. Cuomo’s whitewash of the numbers.  
Haydee Pabey and Alexa Rivera showed Gov. Hochul pictures of their moms Elba and Ana while sharing their tragic stories. 

      New York Gov. Kathy Hochul speaks to reporters after a ceremonial swearing-in ceremony at the state Capitol, Tuesday, Aug. 24, 2021, in Albany, N.Y. 
      (AP Photo)
Gov. Hochul says that going forward, her administration is going to transparent.  She gave us her word that her administration would work with us. 
She looked us in the eye and thanked us for being strong, relentless advocates.
Cuomo wanted everyone to believe this was about politics. It never was. There were no Democrats or Republicans in that room pouring their hearts out.
It was about human beings wanting to help and listening to those that were hurting.
I left the meeting with a glimmer of hope. That’s something I haven’t had in a long time. 
But, Gov. Hochul’s actions in the days ahead will speak louder than words. 
An apology won’t bring back our loved ones, but it might just change the way things are done going forward to protect other families in the future. 
Get the recap of top opinion commentary and original content throughout the week.
Subscribed

The United States is donating millions of doses of the Johnson & Johnson COVID-19 vaccine to the African Union, the White House said Thursday.
The 17 million doses will arrive in the coming weeks. These are in addition to the 50 million doses already sent to the 55-member continental union.
FDA PANEL ENDORSES MODERNA'S COVID-19 BOOSTER VACCINE FOR CERTAIN HIGH RISK GROUPS
The doses will "help close the vaccine equity gap," the White House said in a statement.
The African Union, whose states comprise more than 1.3 billion people, has alleged that manufacturers are not giving its member states adequate access to vaccines. Only 2% of the approximately 5.7 billion doses of COVID-19 vaccines given to people around the world have been in Africa.
The Biden administration has dispatched tens of millions of vaccine doses to other countries through the World Health Organization's COVID-19 Vaccines Global Access (COVAX), which is a worldwide initiative aimed at equitable access to COVID-19 vaccines.
Biden mentioned the donation during a bilateral press conference with Kenyan President Uhuru Kenyatta in the Oval Office on Thursday.
"We're continuing our shared fight against COVID," said Biden. "The United States has donated 2.8 million doses of vaccine to Kenya as part of a 50 million doses we've donated to the African Union.
"And I'm proud to announce that today that we're making an additional, historic one-time donation of 17 more million doses of J&J vaccine to the AU, and we're going to be sending some more of it by the end of the year to Kenya."
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Atlanta Braves are preparing to play without outfielder Jorge Soler in the NL Championship Series as they await his clearance following his positive COVID-19 test.
The Braves worked out Thursday at Truist Park without Soler, who was pulled from the lineup for Game 4 of the NL Division Series against Milwaukee on Tuesday. Dansby Swanson replaced Soler as the leadoff hitter, Guillermo Heredia moved into the lineup in center field and Cristian Pache took Soler’s spot on the 26-man roster.
Playing with the adjusted lineup, the Braves beat the Brewers 5-4 to clinch the best-of-five division series.
Braves manager Brian Snitker would like to have Soler's power bat on his roster for the Championship Series. Soler hit a combined .223 with 27 homers and 70 RBIs with Kansas City and Atlanta during the regular season.
"We want everybody there," Snitker said when asked about Soler, adding he "hated that he had to miss that" clinching game against the Brewers.
"I don’t know that this team has been dependent, as we’ve shown, on one guy all year, quite honestly. The guys keep playing the game. Would you like to have him? Yeah. If we don’t, so be it. Just go out and win however else we can."
Soler has been vaccinated but may not be cleared to return until after the best-of-seven NLCS. Snitker said he has not talked with Soler.
"We’ve got to approach it like I don’t know if he’ll be here for the NLCS," Snitker said. "That’s how we have to approach it. Until he shows up and is cleared and does everything that MLB needs him to do, we’re going to look like it's like he’s not going to be here."
Soler was part of the dramatic outfield makeover orchestrated by general manager Alex Anthopoulos after the Braves lost Ronald Acuña Jr. to a season-ending knee injury and Marcell Ozuna to legal troubles.
Anthopoulos first acquired Joc Pederson and then added Soler, Eddie Rosario and Adam Duvall near the July 30 trade deadline.
The outfield depth created by the moves becomes even more important with Soler's status uncertain as the Braves try to return to the World Series for the first time since 1999.
"I think when we got Joc the clubhouse was like ‘we’re not going to sit around and wait,’" Snitker said. "Alex is on the move. He was striking fast and when he did that — the next wave of guys at the deadline — it showed our guys we were seriously in this thing. I think it did the world of good for that room in there."
The Braves may stick with their three-man rotation of Charlie Morton, Max Fried and Ian Anderson. Morton pitched on short rest on Tuesday, allowing two runs in 3 1/3 innings. Fried is the probable Game 1 starter in the NLCS.
Huascar Ynoa and Drew Smyly, who were part of the regular-season rotation, were in the bullpen in the division series and seem likely to be available again in relief. They could be used as part of a bullpen approach in Game 4.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Brooklyn Nets won’t allow Kyrie Irving to participate in any team activities until he gets the COVID-19 vaccine, the team announced Tuesday morning. 
Nets general manager Sean Marks released a statement confirming Irving’s status with the team amid controversy that the Nets’ star player is reportedly unwilling to get the vaccine. 
IRVING COULD JOIN NETS AT PRACTICE AFTER RULING FROM CITY
"Given the evolving nature of the situation and after thorough deliberation, we have decided Kyrie Irving will not play or practice with the team until he is eligible to be a full participant," the statement read. 

      Brooklyn Nets guard Kyrie Irving, left, drives downcourt against Sacramento Kings guard De'Aaron Fox during the first half of an NBA basketball game in Sacramento, Calif., Monday, Feb. 15, 2021. (AP Photo/Rich Pedroncelli)
      
"Kyrie has made a personal choice, and we respect his individual right to choose. Currently, the choice restricts his ability to be a full-time member of the team, and we will not permit any member of our team to participate with part-time availability."
The Nets were initially preparing to start the season without Irving playing home games due to New York City health mandates. He was at risk of missing 41 games and was granted permission to practice with the team at its facilities in New York but Tuesday’s announcement makes him ineligible for any team activity until he complies. 

      Brooklyn Nets guard Kyrie Irving reacts to missing a shot during the second half of the team's NBA basketball game against the Atlanta Hawks, Friday, Jan. 1, 2021, in New York. (AP Photo/Adam Hunger)
      
"It is imperative that we continue to build chemistry as a team and remain true to our long-established values of togetherness and sacrifice," Marks continued. "Our championship goals for the season have not changed, and to achieve these goals each member of our organization must pull in the same direction. We are excited for the start of the season and look forward to a successful campaign that will make the borough of Brooklyn proud."

      Sacramento Kings forward Marvin Bagley III tries to steal the ball from Brooklyn Nets guard Kyrie Irving (11) during the first half of an NBA basketball game, Tuesday, Feb. 23, 2021, in New York, as Sacramento Kings guards DaQuan Jeffries (19) and Buddy Hield (24) watch from the floor. (AP Photo/Kathy Willens)
      
Irving has not confirmed his vaccine status but asked the media for privacy regarding the matter during the Nets media week. 
The NBA has announced that players who miss games because of local health mandates will not be paid.
Senior fellow at the Hoover institute Victor Davis Hanson calls out Fauci for ignoring science on coronavirus
A federal judge in New York granted a preliminary injunction Tuesday in favor of 17 health care workers applying for religious exemptions to the state's COVID-19 mandate.
U.S. District Judge David Hurd's injunction, which is effective statewide, temporarily bars New York State from forcing employers to fire medical workers seeking a religious exemption.
"The question presented by this case is not whether plaintiffs and other individuals are entitled to a religious exemption from the State’s workplace vaccination requirement," Hurd wrote.
"Instead, the question is whether the State’s summary imposition of [the mandate] conflicts with plaintiffs’ and other individuals’ federally protected right to seek a religious accommodation from their individual employers," he continued, adding, "The answer to this question is clearly yes."
NY GOVERNOR REFUSING TO BUDGE ON VACCINE MANDATE FOR NURSES: YOU'RE REPLACEABLE
Hurd also left the door open for an appeal, writing, "Because the issues in dispute are of exceptional importance to the health and the religious freedoms of our citizens, an appeal may very well be appropriate."
The New York State Department of Health issued an emergency regulation Aug. 26 mandating that most healthcare workers must be vaccinated against COVID-19 by Sept. 27 or face termination. On Sept. 14, attorneys with the Thomas More Society filed a suit on behalf of 17 Roman Catholic and Baptist medical workers, alleging discrimination and constitutional violation.
"With this decision the court rightly recognized that yesterday’s ‘front line heroes’ in dealing with COVID cannot suddenly be treated as disease-carrying villains and kicked to the curb by the command of a state health bureaucracy," said Thomas More Society Special Counsel Christopher Ferrera, who represented the plaintiffs in the case.
"Some of these plaintiffs contracted COVID while treating patients, recovered, and were allowed to return to work with the same protective measures that were good enough for the 18 months that they were the heroes in the battle against the virus. There is no ‘science’ to show that these same measures are suddenly inadequate – especially when they are allowed for those with medical exemptions," he added.
Gov. Kathy Hochul, D-N.Y., defended the mandate in a Tuesday statement about the order.
"My responsibility as Governor is to protect the people of this state, and requiring health care workers to get vaccinated accomplishes that," she said. "I stand behind this mandate, and I will fight this decision in court to keep New Yorkers safe."
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
The Idaho governor on Wednesday issued an executive order repealing his political rival’s executive order from the previous day involving COVID-19 vaccine passports and mandatory testing. 
Republican Gov. Brad Little issued the order while still in Texas, a move that challenges the state’s longstanding practice of making the lieutenant governor acting governor when the governor is out of state. 
Lt. Gov. Janice McGeachin, a far-right Republican who is running to take Little’s job, issued her order Tuesday and also sought to activate the Idaho National Guard and send soldiers to the U.S.-Mexico border. 

      Idaho Gov. Brad Little at a March 2020 news conference.
      ((Darin Oswald/Idaho Statesman/Tribune News Service via Getty Images))
COVID-19 SURVIVORS IN DANGER OF HEART DAMAGE YEAR AFTER INFECTION, REPORT SAYS 
Little is in Texas meeting with nine other Republican governors over concerns on how President Joe Biden is handling border issues. In Idaho, the governor and lieutenant governor don’t run on the same ticket. Little was expected back late Wednesday. 
Little’s executive order appears to lay the groundwork for a court challenge to determine who is in charge when governor leaves the state. 
Little’s order states that he did not authorize McGeachin to act, and it cites Idaho law. 
"Nor does my temporary presence in Texas on official business impair my ability to represent the people of Idaho thus necessitating action by another executive to ensure the continuity of state government," the executive order states. 
The order also notes that Little had previously through an executive order banned state entities from requiring vaccine passports. 

      Republican Lt. Gov. Janice McGeachin addresses a rally in Boise on Sept. 15.
      (AP)
Little’s order also states that McGeachin’s order prohibiting COVID-19 testing would harm the state’s ability to curb the spread of the disease. 
Idaho is currently under crisis standards of care because of unvaccinated COVID-19 patients filling hospitals. Nearly 3,000 people have died from the disease in the state. 
Little’s office declined to comment about his executive order. 
McGeachin’s office didn’t return a call from The Associated Press. 
The attorney general’s office, which would appear to have to defend the state’s top executive in the dispute, declined to comment. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Washington, D.C., city officials said nearly 2,500 health care workers have failed to comply with their COVID-19 mandate deadline requiring at least one dose of the inoculation by Thursday. Nearly 70% of those health care workers who have not yet been vaccinated have requested religious exemptions. 
City Administrator Kevin Donahue said the largest number of exemption requests have come from the D.C. Fire and EMS Department, The Washington Post reported. About 267 of the agency’s some 2,000 employees have sought some type of exemption from the vaccine mandate, with the vast majority of that group citing their religion. All 20 requests which have been reviewed so far have been rejected. 
NORTH CAROLINA HOSPITAL SYSTEM NOVANT HEALTH TO FIRE 175 EMPLOYEES WHO REFUSED COVID VACCINE MANDATE 
Donahue said 89% of all D.C. government employees had reported their vaccination status by Thursday afternoon, with 75% reporting that they were fully vaccinated. During a call Friday, D.C. City Council member Elissa Silverman suggested that the city health department might eliminate the religious exemption for the vaccine mandate, arguing possible abuse. 
But members of the DC Firefighters Bodily Autonomy Affirmation Group, which is made up of members who hold Christian, Jewish and Muslim beliefs, insist that their requests for religious exemptions coincide with genuine expressions of their faith, which has comforted them during the pandemic. The group has retained legal counsel should their requests be denied. 
D.C. Mayor Muriel Bowser announced in August that all licensed, certified health professionals, EMS personnel, as well as unlicensed health care workers, which include patient care technicians, personal care aides, environmental services staff, must start a vaccination dosage by Sept. 30. 
That mandate applies to some 82,000 licensed health care workers, not including fire department personnel, city officials said. 
But just 51,000 licensed health care workers had reported their vaccination status by Friday morning – about 49,000 of which said they had received one or more doses of the vaccine, The Washington Post reported. Meanwhile, some 1,640 licensed health care workers reported that they had not started a dosage – and 75% of that group said they are seeking a religious exemption. 
Of the roughly 13,000 unlicensed health care workers who reported their status to the city, more than 12,000 said they received at least one dose of the vaccine. Meanwhile, 62% of the some 823 unlicensed workers who reported not having received the vaccine are requesting a religious exemption.
Donahue said each exemption request must be reviewed on a case-by-case basis under federal law, and there is an appeals process, WTOP reported. But firefighters whose requests are ultimately denied might face termination. Other health care workers might face having their medical licenses revoked. Those workers who might appeal the decision will continue to be subjected to weekly testing.   
Danielle Wallace is a Digital Reporter for Fox News and FOX Business. Follow her on Twitter at @danimwallace. If you have a tip, you can email her at danielle.wallace@fox.com.
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Former NBA player Lazar Hayward was reportedly arrested in Hawaii last week after allegedly falsifying COVID test results to avoid quarantine.
Hayward, 34, and another person he was traveling with were arrested at Lihue Airport in Kauai Tuesday after police were notified that the pair uploaded fake negative COVID test results into the state’s Safe Travels portal, Hawaii News Now reported. 
NUGGETS' MICHAEL PORTER JR. DOESN’T ‘FEEL COMFORTABLE' WITH COVD VACCINE, WOULDN’T SUPPORT LEAGUE MANDATE
The former Minnesota Timberwolves forward was charged with unsworn falsification, the station reported. 

      Lazar Hayward of the Minnesota Timberwolves drives against the Utah Jazz at Energy Solutions Arena on Jan. 2, 2013 in Salt Lake City, Utah.
      (Photo by Melissa Majchrzak/NBAE via Getty Images)
Police said Hayward uploaded the bogus documents to avoid quarantine. He was later released and returned to the airport, where he took a direct flight to Los Angeles. 

      Lazar Hayward of the Oklahoma City Thunder shoots against the Milwaukee Bucks on April 9, 2012 at the Bradley Center in Milwaukee, Wis.
      (Photo by Gary Dineen/NBAE via Getty Images)
Hayward was drafted by the Washington Wizards in 2010 but was traded to the Timberwolves shortly after. He played one season before getting traded to the Oklahoma City Thunder. He briefly returned to Minnesota in 2013 before spending time in the G League. 

      Hayward had a brief NBA career.
      (Action Images / Paul Harding)
Hawaii requires a 10-day traveler quarantine. An Illinois woman was recently arrested after she uploaded a fake vaccine card that was flagged after the vaccine maker Moderna was misspelled, the New York Post reported. 
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
San Jose Sharks star Evander Kane was suspended 21 games on Monday for submitting a fake COVID-19 vaccination card, the NHL announced.
Kane will not be able to play prior to San Jose’s Nov. 30 game against the New Jersey Devils.

      In this May 12, 2021, file photo, San Jose Sharks' Evander Kane (9) during an NHL hockey game against the Vegas Golden Knights in San Jose, Calif. The NHL has suspended Kane for 21 games for submitting a fake COVID-19 vaccination card. The league announced the suspension without pay on Monday, Oct. 18, 2021, and said Kane will not be eligible to play until Nov. 30 at New Jersey.
      (AP Photo/Jeff Chiu, File)
"The National Hockey League announced today that San Jose Sharks forward Evander Kane has been suspended for 21 regular-season games, without pay, for an established violation of, and lack of compliance with, the NHL/NHLPA COVID-19 Protocol. Under the terms of the Collective Bargaining Agreement, the forfeited pay goes to the Players’ Emergency Assistance Fund," the NHL said.
Kane will forfeit about $1.68 million of his $7 million salary. Using a fake vaccination card is illegal in the U.S. and Canada and is against NHL rules.

      San Jose Sharks left wing Evander Kane (9) before the game against the Colorado Avalanche at Ball Arena April 30, 2021, in Denver, Colorado.
      (Isaiah J. Downing-USA TODAY Sports)
FORMER NHL PLAYER JIMMY HAYES DIED FROM 'ACUTE INTOXICATION' DUE TO FENTANYL AND COCAINE, FAMILY SAYS
The league also said its investigation into allegations of sexual and physical abuse made against Kane by his estranged wife, Anna, could not be substantiated. He had previously been cleared by the league after an investigation into allegations he was betting on games. The claim was made by Anna Kane as well.

      San Jose Sharks left wing Evander Kane (9) falls to the ice during the third period of the team's NHL hockey game against the Vegas Golden Knights, Thursday, Nov. 21, 2019, in Las Vegas. 
      (AP Photo/John Locher)
"The NHL has advised our organization that Evander Kane has been suspended without pay for 21 games for an established violation of, and lack of compliance with, the NHL/NHLPA COVID-19 Protocols," the Sharks said in a statement.
"While we are encouraged by Evander’s commitment to moving forward, we are extremely disappointed by his disregard for the health and safety protocols put in place by the NHL and the NHLPA."
Kane is entering his fourth season with the Sharks. In 56 games last season, he scored 22 goals and racked up 27 assists.
The Associated Press contributed to this report.
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Health officials will update mask guidance as COVID-19 cases and hospitalizations continue a downward trend, but the upcoming "respiratory virus" season may give them pause. 
The White House COVID-19 Response Team and public health officials spoke with reporters during a press conference Friday. The team touted the incredible progress made thanks to the push on vaccinations and introduction of booster shots, with 10 million booster shots administered nationwide as of last week. 

      CDC Director Dr. Rochelle Walensky answers questions from reporters during a Friday press conference. 
      (Courtesy White House YouTube channel)
However, Centers for Disease Control and Prevention Director Dr. Rochelle Walensky noted that officials will need to take the upcoming threat of respiratory viruses into consideration before updating mask guidance. 
FLORIDA'S NEW SURGEON GENERAL: DATA DOES NOT SUPPORT MASK MANDATES IN SCHOOL
"We still have 75,000 cases in this country, and I am very encouraged to watch these trends coming down, but as you know we still have over 90% of our counties that are in high-risk or high-transmission," Walensky told reporters. "As we watch the community levels come down we will update our recommendations." 
"It’s important to note that as we look at the current situation we are also heading into respiratory virus season," Walensky added. "During that season we know respiratory viruses tend to thrive, so we’re taking that all into consideration."
WHEN IS IT TIME TO GET THE COVID-19 BOOSTER SHOT?
"Respiratory virus season" typically begins in the fall – in October or November – and ends in spring – in February or March – meaning the CDC may not ease back on mask guidance until the spring season.
Current mask guidance from the CDC recommends that individuals who are not fully vaccinated and aged 2 or older should wear masks in indoor public spaces. 
CDC GUIDELINES FOR 2021 HOLIDAYS: HOW TO CELEBRATE SAFELY
The CDC recommends that individuals who are fully vaccinated but in an area of substantial or high transmission should wear a mask as well, but some private businesses do not require them, especially in areas such as New York City where proof of vaccination is required for entry. 
Walensky touted the success of the vaccine booster program, which she credits for a significant drop in COVID-19 cases across the country: In mid-September, the seven-day average for new cases topped around 175,000, but six weeks on the average is down to around 75,000, according to numbers from Our World in Data. 
Some experts have cautioned that a fifth wave of COVID-19 infections may occur in the coming winter season. 
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
Fox News Flash top headlines are here. Check out what's clicking on Foxnews.com.
Stress related to the COVID-19 pandemic has made it harder for Americans to make basic decisions, according to a survey. 
According to an American Psychological Association survey of "Stress in America," millennials were particularly affected, with nearly 50% of more than 3,000 adult respondents reporting that they are struggling with daily tasks as coronavirus continues to spread. 
Comparatively, only 37% of Gen Z, 32% of Gen X, 14% of boomers and 3% of older adults reported the same.
Nearly a third of adults who took the online August/COVID Resilience Survey conducted by The Harris Poll said sometimes they are so stressed about the pandemic that they struggle to make basic decisions and more than a third of them said it has been more stressful to make day-to-day decisions and major life decisions in comparison to life before the pandemic.
DEPRESSION, ANXIETY FELL AS US COVID-19 RESTRICTIONS ENDED IN 2021: CDC DATA
Younger adults were more likely to feel the decisions are more stressful now and more than 60% agreed that the pandemic has made them rethink how they were living their life. 
Sixty-three percent said uncertainty about the near future causes them stress and around half said the pandemic had made planning for the future feel impossible.
"When it comes to overall stress, it is not surprising to find that younger generations, who were more likely to say they struggle with basic decisions, also reported generally high stress levels," the survey said. 
Gen Z adults, millennials and Gen Xers reported higher average stress levels over the past month related to the pandemic than boomers and older adults, and around half of Gen Z adults and millennials admitted that they do not know how to manage the stress they feel due to the pandemic.
Decision-making fatigue is having a disproportionate impact on parents – especially those with younger children.
Additionally, pandemic stress among people of color is still elevated, especially for Hispanic and Black adults. 
Hispanic adults reported the highest levels of stress, on average, over the past month related to the pandemic and the survey said those conclusions were "not surprising, considering findings from the survey that shine a light on racial and ethnic disparities in relation to the impact of the pandemic."
UNC CHAPEL HILL CANCELS CLASSES AMID SUICIDE FEARS, MENTAL HEALTH CRISIS
"Specifically, Hispanic adults were more likely than non-Hispanic White adults to know someone who had been sick with or died of COVID-19," the survey noted. 
Stress levels remain higher than pre-pandemic levels and work- and housing costs-related stress slightly increased from last year, although there was a significant downward trend across most factors in the same time frame.
As a result of all of this stress, nearly three-quarters of U.S. adults said they have experienced various health impacts like headaches, feeling overwhelmed. fatigue and changes in sleeping habits.
Eighty-six percent of millennials reported impacts of stress, closely followed by 84% of Gen Z adults and 77% of Gen Xers. Less than 60% of boomers and older adults said the same.
Behavioral changes were also reported as a result of stress, including avoiding social situations, altering eating habits, procrastinating or neglecting responsibilities, or altering physical activity levels.
More than one-third said they stress ate during the first year of the pandemic.
Lastly, over half of U.S. adults said they were struggling with the pandemic's ups and downs, with most having average resilience scores and just 16% having high resilience scores.
Nevertheless, overall, the survey found that stress levels are holding steady and that U.S. adults retain a positive outlook. 
Seventy percent were confident that everything would work out at the pandemic's conclusion and 77% said they were generally faring well.
Stay up-to-date on the biggest health and wellness news with our weekly recap.
Subscribed
New York Congresswoman Elise Stefanik says Republicans will stand up for American's freedoms against forced vaccines.
New York Congresswoman Elise Stefanik called President Biden's vaccine mandate "unconstitutional" and warned that it is only making the current labor shortage worse. On "The Faulkner Focus," Stefanik, R-N.Y., said Republicans are opposed to the mandate, which she considers an overreach by the government, and promised to defend Americans' freedoms.
FLORIDA FIRE CHIEF: I WAS FIRED FOR REFUSING TO ENFORCE ‘UNLAWFUL’ VACCINE MANDATE
ELISE STEFANIK: These vaccine mandates, whether at the federal level or some of our Democrat governors are putting them into place, they are unconstitutional and illegal. In my home state of New York, you talked about how we could see massive shortages. We are already seeing worker shortages in New York with our unconstitutional mandate. I represent a hospital in my district, in a rural region, Louis County. They're no longer able to deliver babies because of this vaccine mandate. So our workers – whether it's our nurses, our doctors, our first responders, our law enforcement officers – they worked, they put their lives and health on the line throughout the COVID pandemic. And now these mandates are forcing them out of a job.
If they choose not to get the vaccine, that is their personal choice. That is already exacerbating a labor shortage that we're already facing in this country, particularly as we're heading into the holidays with such a significant supply chain crisis. So Republicans are opposed to these top-down mandates. This is government overreach at its worst. And what was most frustrating and telling for me to hear from the president of the United States is he mocked Americans for standing up for their freedoms. This country is based upon freedoms and Republicans are going to defend freedom. 
WATCH THE FULL INTERVIEW BELOW:
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
Paul Gigot interviews Dr. Marty Makary
COVID has given us a clear-eyed look at a broken Food and Drug Administration that’s mired in politics and red tape. 
Americans can now see why medical advances often move at turtle speed. We need fresh leadership at the FDA to change the culture at the agency and promote scientific advancement, not hinder it.
This starts at the top. Our public health leaders have become too be accepting of the bureaucratic processes that would outrage a fresh eye. For example, last week the antiviral pill Molnupiravir was found to cut COVID hospitalizations in half and, remarkably, no one who got the drug died. 
The irony is that Molnupiravir was developed a year ago. Do the math on the number of lives that could have been saved if health officials would have moved fast, allowing rolling trials with an evaluation of each infection and adverse event in real-time. Instead, we have a process that resembles a 7-part college application for each of the phase 1, 2, and 3 clinical trials. 
DR. MARTY MAKARY: I HAVE MEDICAL CONCERNS AROUND BIDEN'S NEW VACCINE MANDATES
The FDA is now in receipt of Molnupiravir’ application for an EUA, which the agency will ponder for the next two to three months. Authorization of this life-saving drug is expected just when the last Covid wave will be over. We can’t use peacetime processes in a time of war.
For too long, FDA leaders have acted like a crusty librarian who gets annoyed when someone wants to borrow a book. But then give preference to people they like. 
For example, why hasn’t the FDA granted an emergency use authorization for the Oxford/AstraZeneca vaccine? The U.K. approved it last year and more than a billion doses have been delivered worldwide. We badly needed that life-saving vaccine back when American seniors were dying by the thousands each day and we were rationing our limited supply.
The FDA needs a change in culture. The status quo is defined by counterproductive rigidity and a refusal to adapt. For example, since the FDA first authorized a COVID vaccine, ample data has demonstrated that spacing out the first two doses of a Covid vaccine by a few months or more generates stronger immunity—a principle that’s true for any vaccine in medicine. In the case of the Pfizer vaccine, waiting three months between the first and second dose results in 3.5-times the immunity.
Yet the FDA is absolute that people still must get their second mRNA dose at 3 or 4 weeks after the first because that’s how its committee first voted to authorize them. The new data are clear, everyone should be encouraged to space out their first two vaccine doses by months instead of weeks. Doing so would likely obviate the need for a booster in the future. It’s absolutely mind boggling to me and many others that the FDA still insists that people show up 3 weeks after their first Pfizer vaccine dose when we should be urging people to come back at 3 months.
In 1995, despite scant data to support OxyContin as a treatment for chronic pain, the FDA granted the drug full approval, helping spawn the U.S. opioid crisis. Ever wonder what happened to the FDA regulator who oversaw that approval? She’s now running the agency.
Dr. Janet Woodcock, an agency veteran of 35 years, took the helm in January and presided over the prolonged Johnson & Johnson vaccine pause that cancelled millions of vaccinations and fueled hesitancy. Weeks later, her agency decided to not convene its expert advisory committee when evaluating a COVID vaccine for children 12 to 15. 
Diversity in the leadership of any organization is important because different life experiences can help solve problems and challenge a status quo. But our top FDA and NIH leadership lack minority and age diversity.
Not convening these experts was a convenient way to ignore concern about heart inflammation from the second dose, which is estimated to occur in up to 1 in 6,000 boys. Moreover, the rigid FDA leadership would not consider a single dose of the vaccine for kids, or a modified interval between doses, even in those who had previously had Covid.
Perhaps most disturbing, Dr. Woodcock signed a letter last month calling for booster shots for most Americans starting September 20, ahead of her agency’s evaluation. For the head of the nation’s top drug regulatory agency to issue such a statement, synchronized with a White House push, was unprecedented. 
The FDA’s head of vaccines resigned soon after, along with her deputy director, clearly in protest of the intrusion of politics. They took to the pages of a peer-reviewed journal to detail how the data is simply not there to support boosters for most Americans. It never was. Then after backlash from the medical community, Woodcock and the CDC director publicly warned the White House to back away from the "everyone get boosters" plan. 
In the end, the premature call for boosters distracted Americans from the critical message that vaccines save lives and was tone deaf to calls for global vaccine equity as half the world has no vaccine. Moreover, Americans are confused about the FDA's down vote on Pfizer boosters for the general public while the CDC left the door wide open everyone except for perhaps a young thin forest ranger who works alone.
The FDA also fueled vaccine hesitancy through its bureaucratic delays in approving vaccines. Despite an impeccable safety profile, it took until late August for the Pfizer vaccine to be granted full approval by the agency. Ironically, it came after 363 million Covid vaccine doses were administered in the U.S. The other vaccines still await full approval.
I would not characterize drug approvals coming from the FDA as predictably slow. I would describe them as erratic. Under Woodcock’s leadership a few months ago, the agency granted a full and accelerated approval for an Alzheimer’s drug with zero data to show a clinical benefit. In fact, the FDA’s external experts examining the drug (Abducanumab) voted unanimously (7-0) against approval. Three resigned in protest when the agency ignored their guidance and approved it.
Diversity in the leadership of any organization is important because different life experiences can help solve problems and challenge a status quo. But our top FDA and NIH leadership lack minority and age diversity.
Drs. Woodcock (age 73), Francis Collins (age 71) who recently announced his retirement, and Anthony Fauci (age 80) have valuable wisdom but they are all like-minded, such as in their collective dismissal of natural immunity. Moreover, they seem complacent with our broken health bureaucracies. 
For example, any new leader would be irate to know that the NIH spent twice as much taxpayer money on aging research last year than it did on COVID research. Last year, when the CDC shut children out of public schools, they were all mum. 
It’s time for our old guard medical leaders to step aside into advisory roles and let new scientists, ones who are not afraid to speak up, take charge.
Get the recap of top opinion commentary and original content throughout the week.
Subscribed
In media news today, Katie Couric admits she protected Ruth Bader Ginsburg by editing out remarks on anthem kneelers, a former Obama ethics official slams the Biden White House for avoiding questions on Hunter Biden's artwork, and Facebook says it will treat journalist and activists as public figures
CNN's chief medical correspondent Dr. Sanjay Gupta admitted to podcast host Joe Rogan Wednesday that it was improper for the network to claim Rogan took "horse dewormer" as a COVID treatment. 
On Wednesday's installment of "The Joe Rogan Experience," Rogan grilled the doctor on why someone like him who already had COVID and has antibodies should get vaccinated. 
"By the way, I'm glad you're better," Gupta said. 
"Thank you," Rogan responded. "You're probably the only one at CNN who's glad … The rest of them are all lying about me taking horse medication."
JOE ROGAN BLASTS MEDIA LIES ABOUT HIS COVID TREATMENT: ‘DO I HAVE TO SUE CNN?’
"That bothered you," Gupta said, grinning. 
"It should bother you too," Rogan shot back. "They're lying at your network about people taking human drugs versus drugs for veterinary."
"Calling it a ‘horse dewormer’ is not the most flattering thing, I get that," Gupta conceded. 
"It's a lie," Rogan pushed back. "It's a lie on a news network … and it's a lie that they're conscious of. It's not a mistake. They're unfavorably framing it as veterinary medicine."

(Getty Images)
Gupta pointed to the "snarky" statement released by the FDA saying, "You are not a horse. You are not a cow," in order to encourage people to not take ivermectin, but Rogan remained persistent on calling out CNN's coverage of a drug that's been "given out to billions and billions of people" and resulted in a Nobel Prize.
"Why would they lie and say that's horse dewormer?" Rogan asked. "I can afford people medicine motherf---er. It's ridiculous! It's just a lie! Don't you think that a lie like that is dangerous on a news network when you know that they know they're lying? … Do you think that that's a problem that your news network lies?"
"What did they say?" Gupta asked. 
The podcast host first told Gupta that his ivermectin was "prescribed to me by a doctor," forciverng the CNN correspondent to say the drug "shouldn't be called" horse dewormer. 
JOE ROGAN TORCHES CNN'S BRIAN STELTER: ‘HEY MOTHERF---ER, YOU’RE SUPPOSED TO BE A JOURNALIST'
"Does it bother you that the network you work for out and out lied, just outright lied about me taking horse dewormer?" Rogan grilled Gupta. 
"They shouldn't have said that," Gupta admitted. 
"Why did they do that?" Rogan asked. 
"I don't know," Gupta responded. 
"You didn't ask? You're the medical guy over there!" Rogan exclaimed. 
"I didn't ask," Gupta said. "I should've asked before coming on this podcast."
Gupta denied Rogan's claim that CNN made the claims with "such glee" before playing a clip of "OutFront" anchor Erin Burnett calling ivermectin a "livestock drug." 
"I don't think Erin had glee," Gupta reacted.
"Well, it's more Brian Stelter who was the gleeful one," Rogan replied, referring to CNN's left-wing media guru. "The point is that's a lie."
"It can be used for humans! I get it," Gupta said. 
"Not just could be used for humans, is often used for humans along with all the other drugs that I took. All human drugs," the podcast host said. "They know it's a human drug and they lied. It's defamatory."
"Yeah, they shouldn't have done that," Gupta reiterated. "I don't know if it's defamatory."
"I bet it is," Rogan asserted. "It's a lie."
Rogan went on to knock CNN for not reporting how he tested negative "five days later" and "felt great" following his treatment. 
"My point is you're working for a news organization. If they're lying about a comedian taking horse medication, what are they telling us about Russia? What are they telling us about Syria? Do you understand that that's why people get concerned about the veracity of the news?" Rogan pressed Gupta before the CNN correspondent, again, conceded he did not take a horse dewormer. 
Get all the stories you need-to-know from the most powerful name in news delivered first thing every morning to your inbox
Subscribed
"""
    wordcloud(fox_text)

    import random
    data = [random.gauss(70, 10) for _ in range(50)]
    box_and_whisker(data)