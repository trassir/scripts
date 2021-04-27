# -*- coding: utf-8 -*-
"""
<parameters>
    <company>d.gavrilov</company>
    <title>association_orion</title>
    <version>1.0.8</version>
    <parameter>
        <name>Настройка вывода камер</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>SERVER_ORION</id>
        <name>Сервер с Orion</name>
        <type>server</type>
    </parameter>
    <parameter>
        <id>MON</id>
        <name>Монитор для отображения</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>ALARM_TEMPLATE_AFTER</id>
        <name>Шаблон после тревоги</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>TIMEOUT</id>
        <name>Таймаут до сброса тревоги (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>STOP_SENSOR_TIME</id>
        <name>Задержка на повторную реакцию на событие от датчика (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>EVENT_ORION</id>
        <type>string</type>
        <name>Cобытие</name>
        <value>Armed</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>Логирование</name>
        <type>boolean</type>
        <value>0</value>
    </parameter>
    <parameter>
        <name>Настройка ассоциаций </name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>ORION_1</id>
        <name>Датчик Орион-1</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_1</id>
        <name>Каналы  к Датчику Орион-1</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_2</id>
        <name>Датчик Орион-2</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_2</id>
        <name>Каналы  к Датчику Орион-2</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_3</id>
        <name>Датчик Орион-3</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_3</id>
        <name>Каналы к Датчику Орион-3</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_4</id>
        <name>Датчик Орион-4</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_4</id>
        <name>Каналы к Датчику Орион-4</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_5</id>
        <name>Датчик Орион-5</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_5</id>
        <name>Каналы к Датчику Орион-5</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_6</id>
        <name>Датчик Орион-6</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_6</id>
        <name>Каналы к Датчику Орион-6</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_7</id>
        <name>Датчик Орион -7</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_7</id>
        <name>Каналы к Датчику Орион-7</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_8</id>
        <name>Датчик Орион -8</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_8</id>
        <name>Каналы к Датчику Орион-8</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_9</id>
        <name>Датчик Орион -9</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_9</id>
        <name>Каналы к Датчику Орион-9</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_10</id>
        <name>Датчик Орион -10</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_10</id>
        <name>Каналы к Датчику Орион-10</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_11</id>
        <name>Датчик Орион -11</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_11</id>
        <name>Каналы к Датчику Орион-11</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_12</id>
        <name>Датчик Орион -12</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_12</id>
        <name>Каналы к Датчику Орион-12</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_13</id>
        <name>Датчик Орион -13</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_13</id>
        <name>Каналы к Датчику Орион-13</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_14</id>
        <name>Датчик Орион -14</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_14</id>
        <name>Каналы к Датчику Орион-14</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_15</id>
        <name>Датчик Орион -15</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_15</id>
        <name>Каналы к Датчику Орион-15</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_16</id>
        <name>Датчик Орион -16</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_16</id>
        <name>Каналы к Датчику Орион-16</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_17</id>
        <name>Датчик Орион -17</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_17</id>
        <name>Каналы к Датчику Орион-17</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_18</id>
        <name>Датчик Орион -18</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_18</id>
        <name>Каналы к Датчику Орион-18</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_19</id>
        <name>Датчик Орион -19</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_19</id>
        <name>Каналы к Датчику Орион-19</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_20</id>
        <name>Датчик Орион -20</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_20</id>
        <name>Каналы к Датчику Орион-20</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_21</id>
        <name>Датчик Орион -21</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_21</id>
        <name>Каналы к Датчику Орион-21</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_22</id>
        <name>Датчик Орион -22</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_22</id>
        <name>Каналы к Датчику Орион-22</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_23</id>
        <name>Датчик Орион -23</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_23</id>
        <name>Каналы к Датчику Орион-23</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_24</id>
        <name>Датчик Орион -24</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_24</id>
        <name>Каналы к Датчику Орион-24</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_25</id>
        <name>Датчик Орион -25</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_25</id>
        <name>Каналы к Датчику Орион-25</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_26</id>
        <name>Датчик Орион -26</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_26</id>
        <name>Каналы к Датчику Орион-26</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_27</id>
        <name>Датчик Орион -27</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_27</id>
        <name>Каналы к Датчику Орион-27</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_28</id>
        <name>Датчик Орион -28</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_28</id>
        <name>Каналы к Датчику Орион-28</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_29</id>
        <name>Датчик Орион -29</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_29</id>
        <name>Каналы к Датчику Орион-29</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_30</id>
        <name>Датчик Орион -31</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_30</id>
        <name>Каналы к Датчику Орион-30</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_31</id>
        <name>Датчик Орион -31</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_31</id>
        <name>Каналы к Датчику Орион-31</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_32</id>
        <name>Датчик Орион -32</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_32</id>
        <name>Каналы к Датчику Орион-32</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_33</id>
        <name>Датчик Орион -33</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_33</id>
        <name>Каналы к Датчику Орион-33</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_34</id>
        <name>Датчик Орион -34</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_34</id>
        <name>Каналы к Датчику Орион-34</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_35</id>
        <name>Датчик Орион -35</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_35</id>
        <name>Каналы к Датчику Орион-35</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_36</id>
        <name>Датчик Орион -36</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_36</id>
        <name>Каналы к Датчику Орион-36</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_37</id>
        <name>Датчик Орион -37</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_37</id>
        <name>Каналы к Датчику Орион-37</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_38</id>
        <name>Датчик Орион -38</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_38</id>
        <name>Каналы к Датчику Орион-38</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_39</id>
        <name>Датчик Орион -39</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_39</id>
        <name>Каналы к Датчику Орион-39</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_40</id>
        <name>Датчик Орион -40</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_40</id>
        <name>Каналы к Датчику Орион-40</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_41</id>
        <name>Датчик Орион -41</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_41</id>
        <name>Каналы к Датчику Орион-41</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_42</id>
        <name>Датчик Орион -42</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_42</id>
        <name>Каналы к Датчику Орион-42</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_43</id>
        <name>Датчик Орион -43</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_43</id>
        <name>Каналы к Датчику Орион-43</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_44</id>
        <name>Датчик Орион -44</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_44</id>
        <name>Каналы к Датчику Орион-44</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_45</id>
        <name>Датчик Орион -45</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_45</id>
        <name>Каналы к Датчику Орион-45</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_46</id>
        <name>Датчик Орион -46</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_46</id>
        <name>Каналы к Датчику Орион-46</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_47</id>
        <name>Датчик Орион -47</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_47</id>
        <name>Каналы к Датчику Орион-47</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_48</id>
        <name>Датчик Орион -48</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_48</id>
        <name>Каналы к Датчику Орион-48</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_49</id>
        <name>Датчик Орион -49</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_49</id>
        <name>Каналы к Датчику Орион-49</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_50</id>
        <name>Датчик Орион -50</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_50</id>
        <name>Каналы к Датчику Орион-50</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_51</id>
        <name>Датчик Орион -51</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_51</id>
        <name>Каналы к Датчику Орион-51</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_52</id>
        <name>Датчик Орион -52</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_52</id>
        <name>Каналы к Датчику Орион-52</name>
        <type>objects</type>
    </parameter>
>
    <parameter>
        <id>ORION_53</id>
        <name>Датчик Орион -53</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_53</id>
        <name>Каналы к Датчику Орион-53</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_54</id>
        <name>Датчик Орион -54</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_54</id>
        <name>Каналы к Датчику Орион-54</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_55</id>
        <name>Датчик Орион -55</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_55</id>
        <name>Каналы к Датчику Орион-55</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_56</id>
        <name>Датчик Орион -56</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_56</id>
        <name>Каналы к Датчику Орион-56</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_57</id>
        <name>Датчик Орион -57</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_57</id>
        <name>Каналы к Датчику Орион-57</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_58</id>
        <name>Датчик Орион -58</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_58</id>
        <name>Каналы к Датчику Орион-58</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_59</id>
        <name>Датчик Орион -59</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_59</id>
        <name>Каналы к Датчику Орион-59</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_60</id>
        <name>Датчик Орион -60</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_60</id>
        <name>Каналы к Датчику Орион-60</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_61</id>
        <name>Датчик Орион -61</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_61</id>
        <name>Каналы к Датчику Орион-61</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_62</id>
        <name>Датчик Орион -62</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_62</id>
        <name>Каналы к Датчику Орион-62</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_63</id>
        <name>Датчик Орион -63</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_63</id>
        <name>Каналы к Датчику Орион-63</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_64</id>
        <name>Датчик Орион -64</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_64</id>
        <name>Каналы к Датчику Орион-64</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_65</id>
        <name>Датчик Орион -65</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_65</id>
        <name>Каналы к Датчику Орион-65</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_66</id>
        <name>Датчик Орион -66</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_66</id>
        <name>Каналы к Датчику Орион-66</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_67</id>
        <name>Датчик Орион -67</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_67</id>
        <name>Каналы к Датчику Орион-67</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_68</id>
        <name>Датчик Орион -68</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_68</id>
        <name>Каналы к Датчику Орион-68</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_69</id>
        <name>Датчик Орион -69</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_69</id>
        <name>Каналы к Датчику Орион-69</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_70</id>
        <name>Датчик Орион -70</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_70</id>
        <name>Каналы к Датчику Орион-70</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_71</id>
        <name>Датчик Орион -71</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_71</id>
        <name>Каналы к Датчику Орион-71</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_72</id>
        <name>Датчик Орион -72</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_72</id>
        <name>Каналы к Датчику Орион-72</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_73</id>
        <name>Датчик Орион -73</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_73</id>
        <name>Каналы к Датчику Орион-73</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_74</id>
        <name>Датчик Орион -74</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_74</id>
        <name>Каналы к Датчику Орион-74</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_75</id>
        <name>Датчик Орион -75</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_75</id>
        <name>Каналы к Датчику Орион-75</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_76</id>
        <name>Датчик Орион -76</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_76</id>
        <name>Каналы к Датчику Орион-76</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_77</id>
        <name>Датчик Орион -77</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_77</id>
        <name>Каналы к Датчику Орион-77</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_78</id>
        <name>Датчик Орион -78</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_78</id>
        <name>Каналы к Датчику Орион-78</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_79</id>
        <name>Датчик Орион -79</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>CHANNEL_79</id>
        <name>Каналы к Датчику Орион-79</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>ORION_80</id>
        <name>Датчик Орион -80</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_80</id>
        <name>Каналы к Датчику Орион-80</name>
        <type>objects</type>
    </parameter>
    <resources>
        <resource>helpers.py</resource>
        <resource>script_object.py</resource>
        <resource>base_object/base_object.py</resource>
        <resource>base_object/icons.py</resource>
        <resource>base_object/__init__.py</resource>
    </resources>
</parameters>
"""

resources = {
    "helpers.py": """
        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
        wYTfceCLK89o/wEf6+v+
    """,
    "script_object.py": """
        eNp1UU1rwzAMvQfyH4RgYEMoa3cr9NCxssMOPRR2Da6jNNmcONhuf//8kSztwnSSn56epGdE
        fKNaXJUDK007ONDnL5IOEfMsz2qjOzgLS2WCoe0GbRy8eugYkQJOTjgK5DyTSlgLpyiUymxm
        8m2egY9I6kVHsANMXEwVG5Ssh1l6h4jqDBsSyjVYAIvA6lOoq4ePH8jHDSboYIw2yDkvFiKy
        IflddrSQWS9Unu8UeDgtJBXVULeGSrpR78rbhllSdQEdWSsuVIBsRN+T2qGfUAknfDJdHcKb
        +k49GT8HnPEutGZyPSpOc0LszcXetYYYxwCzzvAtHELLDA5r/kgfl4n0AvTgWt0L9dvox2vZ
        +lWqmTls/miEI/4TSLXhhT8cOD+CN6s7u9j42Vt4WuPStOSYF/sBmf27sg==
    """,
    "base_object/base_object.py": """
        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
        EkHkX2sKawY=
    """,
    "base_object/icons.py": """
        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
        Pf4f0wLnTA==
    """,
    "base_object/__init__.py": """
        eNpLK8rPVdBTyMwtyC8qUchMzs8r5uVKAwsmJRanxucnZaUml8DknYBC/mARHQXXstQ8IBVc
        kliSyssFAJ8YGOM=
    """,
}
t1utils.resources_check(script_path, resources)

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)
SERVER_ORION = GLOBALS.get("SERVER_ORION", "")
MON = GLOBALS.get("MON", 1)
ALARM_TEMPLATE_AFTER = GLOBALS.get("ALARM_TEMPLATE_AFTER", "")
TIMEOUT = GLOBALS.get("TIMEOUT", 1)
STOP_SENSOR_TIME = GLOBALS.get("STOP_SENSOR_TIME", 1)
EVENT_ORION = GLOBALS.get("EVENT_ORION", "Взять под охрану")

import helpers

helpers.set_script_name()
logger = helpers.init_logger("association_orion", debug=DEBUG)

import host
import json
from script_object import ScriptObject
from datetime import datetime, timedelta

orion_event = None
if EVENT_ORION:
    orion_event = set(ev_type.strip() for ev_type in EVENT_ORION.split(","))
else:
    raise ValueError("Необходимо указать события!")

obj = ScriptObject()


class AlarmMonitor:
    """
    Loop show channel and check old
    """

    def __init__(self, attention_monitor, alarm_template_after, time_to_del):
        self.attention_monitor = attention_monitor
        self.operate_gui = host.object("operatorgui_" + host.settings("").guid)
        self.chan_on_template = []
        for tmpl in host.settings("templates").ls():
            if tmpl.type == "Template" and tmpl.name == alarm_template_after:
                alarm_template_after_content = tmpl["content"]
                break
        else:
            raise RuntimeError("Шаблон не найден")

        self.alarm_template_after = alarm_template_after
        self.alarm_template_after_content = alarm_template_after_content
        self.time_to_del = time_to_del
        self.time_dict = {}

    def attention(self, guid_list):
        self.time_dict[datetime.now()] = guid_list
        for guid in guid_list:
            if guid in self.chan_on_template:
                logger.debug("has already")
                continue
            self.chan_on_template.append(guid)
        logger.debug(self.chan_on_template)
        self.show_chans()

    def show_chans(self):
        logger.debug("go to show %s" % self.chan_on_template)
        if len(self.chan_on_template) > 9:
            self.del_old()
            return
        try:
            self.operate_gui.show(
                "gui7(DEWARP_SETTINGS,,,-1,%s)"
                % ",".join(str(x) for x in self.chan_on_template),
                self.attention_monitor,
            )
        except Exception as e:
            logger.debug("ERROR to assign channels: %s" % e)
        host.timeout(1000 * self.time_to_del, self.del_old)

    def del_old(self):
        for time_, list_ in self.time_dict.copy().iteritems():
            if time_ + timedelta(seconds=self.time_to_del) < datetime.now():
                for channel in list_:
                    if channel in self.chan_on_template:
                        self.chan_on_template.remove(channel)
                del self.time_dict[time_]
        if not self.chan_on_template:
            logger.debug("stop alarm")
            self.operate_gui.show_template(
                self.alarm_template_after, self.attention_monitor
            )
            self.operate_gui.show(
                self.alarm_template_after_content, self.attention_monitor
            )


class OrionArmed:
    """collect orion association dict and catch event orion"""

    def __init__(
        self,
        monitor,
        alarm_template_after,
        time_to_del,
        stop_sensor_time,
        server_orion,
    ):
        self.orion_assotiation = {}
        self.temp_dict = {}
        self.stop_sensor_time = stop_sensor_time
        self.server_orion = server_orion
        self.alarm_obj = AlarmMonitor(monitor, alarm_template_after, time_to_del)
        self.__collect_orion()

    def __collect_orion(self):

        for x in xrange(1, 10000):
            sensor = GLOBALS.get("ORION_%s" % x)
            channels = GLOBALS.get("CHANNEL_%s" % x)
            if sensor is None:
                break

            if not sensor or not channels:
                continue

            sensor_guid = self.find_sensor(sensor)
            channel_guid_list = self.find_channel(channels)
            self.orion_assotiation[sensor_guid] = channel_guid_list
        logger.debug(self.orion_assotiation)
        assert self.orion_assotiation, "Необходимо выбрать датчик!"

    def find_sensor(self, name_orion):
        sensor_guid = ""
        for sett_orion in host.settings("/%s/orion" % self.server_orion).ls():
            if sett_orion.type == "OrionNode":
                for sett_sensor in sett_orion.ls():
                    if (
                        sett_sensor.type == "OrionNode"
                        and name_orion == sett_sensor.name
                    ):
                        sensor_guid = sett_sensor.guid
                        break
        return sensor_guid

    @staticmethod
    def check_access(sett):
        try:
            channel_name = sett.name
            return True
        except ValueError:
            pass

    def find_channel(self, str_channel):
        channels_list = str_channel.split(",")
        channels_guid_list = []
        for srv in host.settings("/").ls():
            if srv.type in ["LocalServer", "RemoteServer"]:
                for sett_chan in host.settings("/%s/channels" % srv.guid).ls():
                    if self.check_access(sett_chan):
                        if sett_chan.name in channels_list:
                            channels_guid_list.append("%s_%s" % (sett_chan.guid, srv.guid))
        return channels_guid_list

    def catch_event(self, ev):
        sensor = ev.origin
        if sensor in self.temp_dict:
            if self.temp_dict[sensor] >= datetime.now() - timedelta(
                seconds=self.stop_sensor_time
            ):
                return
        logger.debug(sensor)
        logger.debug(self.temp_dict)
        for sens in self.temp_dict.copy():
            if self.temp_dict[sens] <= datetime.now() - timedelta(
                seconds=self.stop_sensor_time
            ):
                del self.temp_dict[sens]
        alarm_list = self.orion_assotiation.get(sensor)
        logger.debug("%s сработал для каналов %s" % (sensor, alarm_list))
        if alarm_list:
            obj.fire_event_v2("Association Orion", data=json.dumps({"associated_channel": alarm_list, "ev_type": ev.type}))
            self.alarm_obj.attention(alarm_list)
            self.temp_dict[sensor] = datetime.now()
            host.stats()["run_count"] += 1


if not all([ALARM_TEMPLATE_AFTER, SERVER_ORION]):
    raise ValueError("Заполните параметры!")

oa = OrionArmed(MON, ALARM_TEMPLATE_AFTER, TIMEOUT, STOP_SENSOR_TIME, SERVER_ORION)

for event in orion_event:
    host.activate_on_events(event, "", oa.catch_event)
